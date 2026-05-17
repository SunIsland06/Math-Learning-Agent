import json
import requests

import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# 将仓库根目录加入模块搜索路径，便于跨目录导入
sys.path.append(str(Path(__file__).resolve().parents[1]))

from config.globalConfig import get_global_config
from skill.skillCall import SkillCaller, merge_tool_call_delta
from rag.integration import retrieve_context
from mcp_services.mcp_manager import get_mcp_manager
from memory.memory_manager import build_memory_message


class Model:
    def __init__(
        self,
        model_name=None,
        system_prompt=None,
        api_key=None,
        base_url=None,
        default_stream=None,
        timeout=60,
    ):
        # 读取全局配置并初始化模型参数
        config = get_global_config()
        self.api_key = api_key or config.key
        self.base_url = base_url or config.api_url
        self.model_name = model_name or config.model
        self.default_stream = (
            default_stream if default_stream is not None else getattr(config, "stream", None)
        )
        self.timeout = timeout

        # 初始化系统提示词与对话历史
        self.system_prompt = system_prompt or load_system_prompt()
        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.skill_caller = SkillCaller()
        self.enable_thinking = False
        self.thinking_strength = "high"
        self.enable_search = False
        self.enable_memory = False
        self.memory_username = ""
        self._web_refs: List[Dict[str, str]] = []  # 网页搜索引用
    
    def stream_chat_chunks(self, prompt, temperature=0.7, extra_params=None):
        """Yield model output by content chunk."""
        # 记录用户输入
        self.messages.append({"role": "user", "content": prompt})

        # 构建前置消息：长期记忆 + RAG 知识库
        pre_messages = []
        if self.enable_memory and self.memory_username:
            memory_message = build_memory_message(self.memory_username, prompt)
            if memory_message:
                pre_messages.append(memory_message)

        rag_message = self._build_rag_message(prompt)
        if rag_message:
            pre_messages.append(rag_message)

        if pre_messages:
            payload_messages = self.messages[:-1] + pre_messages + [self.messages[-1]]
        else:
            payload_messages = self.messages

        # 构建工具清单（技能 + MCP，MCP 仅在开启搜索时注入）
        tools = self.skill_caller.build_tools()
        if self.enable_search:
            mcp_manager = get_mcp_manager()
            if mcp_manager.is_ready():
                tools = tools + mcp_manager.build_tools()
        payload = {
            "model": self.model_name,
            "messages": payload_messages,
            "temperature": temperature,
            "stream": True,
            "tools": tools,
            "tool_choice": "auto",
        }
        if extra_params:
            payload.update(extra_params)

        # 请求头（隐藏实际 key 只在日志中处理）
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        try:
            full_answer = ""
            full_reasoning = ""
            tool_calls: List[Dict[str, Any]] = []
            has_tool_calls = False

            # 发起流式请求
            res = requests.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=self.timeout,
                stream=True,
            )
            try:
                res.raise_for_status()
            except requests.HTTPError:
                self._log_http_error("chat.completions", payload, headers, res)
                raise
            for line in res.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data: "):
                    continue

                data_str = line[6:]
                if data_str == "[DONE]":
                    break

                try:
                    chunk = json.loads(data_str)
                    delta = chunk["choices"][0].get("delta", {})
                except (json.JSONDecodeError, KeyError, IndexError):
                    continue

                # 解析工具调用增量
                if delta.get("tool_calls"):
                    has_tool_calls = True
                    merge_tool_call_delta(tool_calls, delta["tool_calls"])
                    continue

                # 记录思考过程（如有）
                reasoning_piece = delta.get("reasoning_content", "")
                if reasoning_piece:
                    full_reasoning += reasoning_piece

                # 只在非工具调用阶段输出内容
                content = delta.get("content", "")
                if content and not has_tool_calls:
                    full_answer += content
                    yield content

            # 若模型调用了工具，则先执行工具再进行二次补全
            if has_tool_calls:
                self._log_http_exchange(
                    "chat.completions",
                    payload,
                    headers,
                    res,
                    response_content=full_answer,
                )
                self._append_tool_calls(tool_calls, full_reasoning)
                tool_messages = self._run_tool_calls(tool_calls)
                self.messages.extend(tool_messages)
                yield from self._stream_followup(headers, temperature, extra_params, rag_message)
                # 输出网页搜索引用
                ref_section = self._build_reference_section()
                if ref_section:
                    yield ref_section
                return

            # 记录最终回答到消息历史
            assistant_message = {"role": "assistant", "content": full_answer}
            if full_reasoning:
                assistant_message["reasoning_content"] = full_reasoning
            self.messages.append(assistant_message)
            self._log_http_exchange(
                "chat.completions",
                payload,
                headers,
                res,
                response_content=full_answer,
            )
        except Exception as e:
            yield f"Model request error: {str(e)}"

    def _append_tool_calls(self, tool_calls: List[Dict[str, Any]], reasoning_content: str = "") -> None:
        # 将工具调用写入对话历史
        message: Dict[str, Any] = {"role": "assistant", "tool_calls": tool_calls}
        if reasoning_content:
            message["reasoning_content"] = reasoning_content
        self.messages.append(message)

    def _run_tool_calls(self, tool_calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # 逐个执行工具调用，MCP 工具路由到 MCP 管理器，并提取引用
        tool_messages: List[Dict[str, Any]] = []
        mcp_manager = get_mcp_manager()
        for call in tool_calls:
            function = call.get("function", {})
            name = function.get("name", "")
            arguments = function.get("arguments", "")
            # 判断是否为 MCP 工具
            if mcp_manager.is_ready() and any(
                t["function"]["name"] == name for t in mcp_manager.build_tools()
            ):
                result = mcp_manager.execute_tool(name, arguments)
                # 提取网页搜索引用（用于回答底部展示）
                if name == "web_search":
                    self._extract_web_refs(result)
            else:
                result = self.skill_caller.execute_tool_call(name, arguments)
            tool_messages.append(self.skill_caller.build_tool_message(call.get("id", ""), name, result))

        return tool_messages

    def _extract_web_refs(self, result: str) -> None:
        """从 web_search 结果中提取 URL 引用。"""
        import re
        self._web_refs = []
        # 匹配 "N. title\n   URL: http..." 格式
        pattern = re.compile(r"^\d+\.\s+(.+?)\n\s+URL:\s+(https?://\S+)", re.MULTILINE)
        for match in pattern.finditer(result):
            title = match.group(1).strip()
            url = match.group(2).strip()
            if url not in {r["url"] for r in self._web_refs}:
                self._web_refs.append({"title": title[:100], "url": url})

    def _build_reference_section(self) -> str:
        """构建 DeepSeek 风格的参考来源区域（Markdown 格式）。"""
        if not self._web_refs:
            return ""
        lines = [
            "",
            "---",
            "",
            "**参考来源：**",
            "",
        ]
        for i, ref in enumerate(self._web_refs, 1):
            # 截取域名作为简短显示
            from urllib.parse import urlparse
            try:
                domain = urlparse(ref["url"]).netloc
            except Exception:
                domain = ref["url"]
            lines.append(f"{i}. [{ref['title']}]({ref['url']}) — `{domain}`")
        lines.append("")
        return "\n".join(lines)

    def _stream_followup(self, headers, temperature, extra_params, rag_message=None):
        # 工具调用完成后的二次流式请求
        payload_messages = self.messages

        if rag_message:
            payload_messages = self.messages[:-1] + [rag_message, self.messages[-1]]

        followup_tools = self.skill_caller.build_tools()
        if self.enable_search:
            mcp_manager = get_mcp_manager()
            if mcp_manager.is_ready():
                followup_tools = followup_tools + mcp_manager.build_tools()

        payload = {
            "model": self.model_name,
            "messages": payload_messages,
            "temperature": temperature,
            "stream": True,
            "tools": followup_tools,
            "tool_choice": "auto",
        }
        if extra_params:
            payload.update(extra_params)

        res = requests.post(
            self.base_url,
            json=payload,
            headers=headers,
            timeout=self.timeout,
            stream=True,
        )
        try:
            res.raise_for_status()
        except requests.HTTPError:
            self._log_http_error("chat.completions.followup", payload, headers, res)
            raise
        full_answer = ""
        full_reasoning = ""
        for line in res.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data: "):
                continue

            data_str = line[6:]
            if data_str == "[DONE]":
                break

            try:
                chunk = json.loads(data_str)
                delta = chunk["choices"][0].get("delta", {})
                content = delta.get("content", "")
            except (json.JSONDecodeError, KeyError, IndexError):
                continue

            reasoning_piece = delta.get("reasoning_content", "")
            if reasoning_piece:
                full_reasoning += reasoning_piece

            if content:
                full_answer += content
                yield content

        assistant_message = {"role": "assistant", "content": full_answer}
        if full_reasoning:
            assistant_message["reasoning_content"] = full_reasoning
        self.messages.append(assistant_message)
        self._log_http_exchange(
            "chat.completions.followup",
            payload,
            headers,
            res,
            response_content=full_answer,
        )

    def stream_chat(self, prompt, temperature=0.7, extra_params=None):
        """Backward compatible char-level stream."""
        # 兼容旧的逐字符输出逻辑
        for chunk in self.stream_chat_chunks(prompt, temperature=temperature, extra_params=extra_params):
            for char in chunk:
                yield char

    def _build_rag_message(self, question: str) -> Dict[str, Any] | None:
        # 从向量库检索上下文并拼成系统消息（含学科分类）
        context, sources = retrieve_context(question, top_k=3)
        if not context:
            return None
        sources_text = "；".join(sources) if sources else "unknown"
        content = (
            "【知识库检索结果】请优先依据以下教材片段回答用户问题。"
            "若检索内容与问题无关，可结合自身知识回答。\n\n"
            f"匹配来源：{sources_text}\n\n"
            f"教材片段：\n{context}"
        )
        return {"role": "system", "content": content}

    def reset(self):
        # 重置对话，仅保留系统提示词
        self.messages = [self.messages[0]]

    def _log_http_error(self, tag: str, payload: Dict[str, Any], headers: Dict[str, str], response) -> None:
        # 记录错误请求
        self._write_log(tag, payload, headers, response)

    def _log_http_exchange(
        self,
        tag: str,
        payload: Dict[str, Any],
        headers: Dict[str, str],
        response,
        response_content: str | None = None,
    ) -> None:
        # 记录请求与响应（成功或失败）
        self._write_log(tag, payload, headers, response, response_content=response_content)

    def _write_log(
        self,
        tag: str,
        payload: Dict[str, Any],
        headers: Dict[str, str],
        response,
        response_content: str | None = None,
    ) -> None:
        # 日志写入到 logs 目录，避免泄漏真实 key
        log_dir = Path(__file__).resolve().parents[2] / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / f"deepseek-{datetime.utcnow().strftime('%Y%m%d')}.log"

        safe_headers = dict(headers)
        if "Authorization" in safe_headers:
            safe_headers["Authorization"] = "Bearer ***"

        if response_content is not None:
            body_text = response_content
        else:
            try:
                body_text = response.text
            except Exception:
                body_text = "<unavailable>"

        record = {
            "time": datetime.utcnow().isoformat() + "Z",
            "tag": tag,
            "status_code": getattr(response, "status_code", None),
            "headers": safe_headers,
            "request": payload,
            "response": body_text,
        }

        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False))
            f.write("\n")


def load_system_prompt():
    # 读取系统提示词模板
    prompt_path = Path(__file__).parent.parent / "prompt" / "system.md"
    return prompt_path.read_text(encoding="utf-8").strip()


if __name__ == "__main__":
    model = Model()
    print(model.system_prompt)
