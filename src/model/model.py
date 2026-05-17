"""
LLM 模型封装模块 —— 负责与 DeepSeek API 交互，处理流式对话、工具调用、
RAG 知识库注入、长期记忆注入以及请求日志记录。

核心流程：
1. stream_chat_chunks() 接收用户问题，拼接系统提示词 + 历史消息
2. 注入长期记忆 + RAG 检索结果（如有）
3. 构建工具清单（技能 + MCP 联网搜索），发起流式请求
4. 若模型返回工具调用 → 执行工具 → 二次补全流式输出
5. 所有请求/响应写入日志文件（脱敏处理）
"""

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
from utils.debug_logger import (
    is_debug_enabled, debug_log, log_prompt, log_response,
    log_skill_call, log_rag_retrieve, log_memory_read, log_mcp_call
)

# ---- 性能优化常量 ----
MAX_TOOL_RESULT_LEN = 4000       # 工具结果最大字符数（超出截断）
MAX_HISTORY_MESSAGES = 20        # 最大历史消息数（超出丢弃最早的）
MAX_TOOL_ARGS_IN_FOLLOWUP = 2000 # followup 中工具参数最大长度


class Model:
    """LLM 模型封装 —— 管理与 DeepSeek API 的对话会话。

    Attributes:
        api_key: API 密钥
        base_url: API 端点 URL
        model_name: 模型名称（如 deepseek-chat）
        messages: 对话历史（含 system prompt）
        skill_caller: 技能调用器实例
        enable_thinking: 是否启用深度思考
        enable_search: 是否启用联网搜索
        enable_memory: 是否启用长期记忆
        _web_refs: 网页搜索引用缓存
    """

    def __init__(
        self,
        model_name=None,
        system_prompt=None,
        api_key=None,
        base_url=None,
        default_stream=None,
        timeout=60,
    ):
        """初始化模型实例，优先使用传入参数，否则从全局配置读取。

        Args:
            model_name: 模型名称，默认从 config/global.yml 读取
            system_prompt: 系统提示词，默认加载 src/prompt/system.md
            api_key: API 密钥，默认从 config/global.yml 读取
            base_url: API 端点 URL
            default_stream: 是否默认流式输出
            timeout: HTTP 请求超时秒数
        """
        config = get_global_config()
        self.api_key = api_key or config.key
        self.base_url = base_url or config.api_url
        self.model_name = model_name or config.model
        self.default_stream = (
            default_stream if default_stream is not None else getattr(config, "stream", None)
        )
        self.timeout = timeout

        # 初始化系统提示词与对话历史（messages[0] 始终为 system prompt）
        self.system_prompt = system_prompt or load_system_prompt()
        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.skill_caller = SkillCaller()
        self.enable_thinking = False
        self.thinking_strength = "high"
        self.enable_search = False
        self.enable_memory = False
        self.memory_username = ""
        self._web_refs: List[Dict[str, str]] = []  # 网页搜索引用列表

    def stream_chat_chunks(self, prompt, temperature=0.7, extra_params=None, image_data_list=None):
        """流式对话主入口 —— 逐 chunk 输出模型回复。

        处理流程：
        1. 将用户消息追加到 messages（支持多模态图片输入）
        2. 注入长期记忆 + RAG 知识库上下文
        3. 构建工具清单并发起流式 API 请求
        4. 解析 SSE 流，合并工具调用增量
        5. 若有工具调用 → 执行 → 二次补全
        6. 最终回答写回 messages

        Args:
            prompt: 用户输入文本
            temperature: 采样温度（0~1）
            extra_params: 额外 API 参数（如 thinking 配置）
            image_data_list: [(name, data_uri), ...] 图片附件列表

        Yields:
            文本块（str），供 SSE 流式输出。
        """
        # 构建用户消息（支持多模态：文本 + 图片）
        if image_data_list:
            content_parts = [{"type": "text", "text": prompt}]
            for name, data_uri in image_data_list:
                content_parts.append({
                    "type": "image_url",
                    "image_url": {"url": data_uri, "detail": "high"},
                })
            user_message = {"role": "user", "content": content_parts}
        else:
            user_message = {"role": "user", "content": prompt}

        self.messages.append(user_message)

        # ---- 历史消息长度限制 ----
        if len(self.messages) > MAX_HISTORY_MESSAGES + 1:
            # 保留 system prompt + 最近的消息
            self.messages = [self.messages[0]] + self.messages[-(MAX_HISTORY_MESSAGES):]

        # 构建前置消息：长期记忆 → RAG 知识库
        pre_messages = []
        if self.enable_memory and self.memory_username:
            memory_message = build_memory_message(self.memory_username, prompt)
            if memory_message:
                pre_messages.append(memory_message)
                log_memory_read(self.memory_username, prompt,
                                memory_message["content"].count("记忆"))

        rag_message = self._build_rag_message(prompt)
        if rag_message:
            pre_messages.append(rag_message)

        # 注入位置：system prompt 之后、最近一条用户消息之前
        if pre_messages:
            payload_messages = self.messages[:-1] + pre_messages + [self.messages[-1]]
        else:
            payload_messages = self.messages

        # 构建工具清单（技能 + MCP 联网搜索）
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

        # DEBUG: 记录发送给 LLM 的提示词
        log_prompt("initial", payload_messages, {
            "temperature": temperature, "tools_count": len(tools),
            "enable_search": self.enable_search, "enable_memory": self.enable_memory,
        })

        # 请求头（日志中会脱敏处理 Authorization）
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        try:
            full_answer = ""
            full_reasoning = ""
            tool_calls: List[Dict[str, Any]] = []
            has_tool_calls = False

            # 发起流式 POST 请求
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

            # 逐行解析 SSE 流
            for line in res.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data: "):
                    continue

                data_str = line[6:]  # 去掉 "data: " 前缀
                if data_str == "[DONE]":
                    break

                try:
                    chunk = json.loads(data_str)
                    delta = chunk["choices"][0].get("delta", {})
                except (json.JSONDecodeError, KeyError, IndexError):
                    continue

                # 合并流式工具调用增量（跨多个 chunk 拼接）
                if delta.get("tool_calls"):
                    has_tool_calls = True
                    merge_tool_call_delta(tool_calls, delta["tool_calls"])
                    continue

                # 记录推理内容（深度思考模式），用标记包裹供前端折叠
                reasoning_piece = delta.get("reasoning_content", "")
                if reasoning_piece:
                    if not full_reasoning:
                        yield "<<<THINKING>>>"
                    full_reasoning += reasoning_piece
                    yield reasoning_piece

                # 输出正文内容（工具调用阶段不输出）
                content = delta.get("content", "")
                if content and not has_tool_calls:
                    if full_reasoning and not full_answer:
                        yield "<<<THINKING_END>>>"
                    full_answer += content
                    yield content

            # 工具调用分支：执行工具 → 二次流式补全
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
                # 追加网页搜索引用
                ref_section = self._build_reference_section()
                if ref_section:
                    yield ref_section
                return

            # 普通回答分支：记录到消息历史
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

    # ============================================================
    # 工具调用处理
    # ============================================================

    def _append_tool_calls(self, tool_calls: List[Dict[str, Any]], reasoning_content: str = "") -> None:
        """将模型的工具调用请求写入对话历史。

        Args:
            tool_calls: 合并后的完整工具调用列表
            reasoning_content: 模型推理内容（如有）
        """
        message: Dict[str, Any] = {"role": "assistant", "tool_calls": tool_calls}
        if reasoning_content:
            message["reasoning_content"] = reasoning_content
        self.messages.append(message)

    def _run_tool_calls(self, tool_calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """逐个执行工具调用并返回 tool 角色消息列表。

        MCP 工具（如 web_search）路由到 MCP 管理器执行；
        技能工具路由到 SkillCaller 执行。
        网页搜索结果中的 URL 自动提取到 _web_refs。

        Args:
            tool_calls: 待执行的工具调用列表

        Returns:
            tool 角色消息列表，可直接追加到 messages。
        """
        tool_messages: List[Dict[str, Any]] = []
        mcp_manager = get_mcp_manager()
        for call in tool_calls:
            function = call.get("function", {})
            name = function.get("name", "")
            arguments = function.get("arguments", "")

            # 判断是否为 MCP 工具（当前仅 web_search）
            if mcp_manager.is_ready() and any(
                t["function"]["name"] == name for t in mcp_manager.build_tools()
            ):
                result = mcp_manager.execute_tool(name, arguments)
                log_mcp_call(name, arguments, len(result))
                if name == "web_search":
                    self._extract_web_refs(result)
            else:
                result = self.skill_caller.execute_tool_call(name, arguments)
                log_skill_call(name, arguments, result)

            # 截断过长的工具结果以节省 token
            if len(result) > MAX_TOOL_RESULT_LEN:
                result = result[:MAX_TOOL_RESULT_LEN] + "\n...[结果过长已截断]"

            tool_messages.append(self.skill_caller.build_tool_message(call.get("id", ""), name, result))

        return tool_messages

    def _extract_web_refs(self, result: str) -> None:
        """从 web_search 工具结果中提取 URL 引用。

        匹配格式：序号. 标题\\n   URL: http...

        Args:
            result: web_search 返回的文本结果
        """
        import re
        self._web_refs = []
        pattern = re.compile(r"^\d+\.\s+(.+?)\n\s+URL:\s+(https?://\S+)", re.MULTILINE)
        seen_urls = set()
        for match in pattern.finditer(result):
            title = match.group(1).strip()
            url = match.group(2).strip()
            if url not in seen_urls:
                seen_urls.add(url)
                self._web_refs.append({"title": title[:100], "url": url})

    def _build_reference_section(self) -> str:
        """构建 Markdown 格式的参考来源区域。

        Returns:
            格式化的参考来源 Markdown 文本，无引用时返回空字符串。
        """
        if not self._web_refs:
            return ""
        from urllib.parse import urlparse

        lines = [
            "",
            "---",
            "",
            "**参考来源：**",
            "",
        ]
        for i, ref in enumerate(self._web_refs, 1):
            try:
                domain = urlparse(ref["url"]).netloc
            except Exception:
                domain = ref["url"]
            lines.append(f"{i}. [{ref['title']}]({ref['url']}) — `{domain}`")
        lines.append("")
        return "\n".join(lines)

    # ============================================================
    # 二次补全（工具调用后）
    # ============================================================

    def _stream_followup(self, headers, temperature, extra_params, rag_message=None):
        """工具调用完成后的二次流式请求 —— 将工具结果反馈给模型生成最终回答。

        Args:
            headers: HTTP 请求头
            temperature: 采样温度
            extra_params: 额外 API 参数
            rag_message: 已弃用（RAG 上下文已在首次请求中注入，此处保留仅为兼容）

        Yields:
            文本块（str）。
        """
        # 注意：rag_message 已在首次 stream_chat_chunks 请求中注入到 pre_messages，
        # 此处不应再插入，否则会破坏 assistant(tool_calls)→tool 消息的连续性，
        # 导致 API 400 错误："insufficient tool messages following tool_calls message"
        payload_messages = _trim_tool_args(self.messages)

        # 二次补全仍携带工具清单（支持连续工具调用）
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
                if not full_reasoning:
                    yield "<<<THINKING>>>"
                full_reasoning += reasoning_piece
                yield reasoning_piece

            if content:
                if full_reasoning and not full_answer:
                    yield "<<<THINKING_END>>>"
                full_answer += content
                yield content

        # 记录二次补全结果
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

    # ============================================================
    # 兼容接口
    # ============================================================

    def stream_chat(self, prompt, temperature=0.7, extra_params=None):
        """逐字符流式输出（向后兼容旧接口）。

        对每个 chunk 再做逐字符拆分，供需要逐字符渲染的调用方使用。
        """
        for chunk in self.stream_chat_chunks(prompt, temperature=temperature, extra_params=extra_params):
            for char in chunk:
                yield char

    # ============================================================
    # RAG 知识库注入
    # ============================================================

    def _build_rag_message(self, question: str) -> Dict[str, Any] | None:
        """从 ChromaDB 向量库检索相关教材片段并构建 system 消息。

        Args:
            question: 用户问题文本

        Returns:
            包含检索结果的 system 角色消息字典，无结果时返回 None。
        """
        context, sources = retrieve_context(question, top_k=2)
        log_rag_retrieve(question, sources, len(context))
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

    # ============================================================
    # 会话控制
    # ============================================================

    def reset(self):
        """重置对话 —— 清空历史消息，仅保留系统提示词（messages[0]）。"""
        self.messages = [self.messages[0]]

    # ============================================================
    # 日志记录（脱敏处理）
    # ============================================================

    def _log_http_error(self, tag: str, payload: Dict[str, Any], headers: Dict[str, str], response) -> None:
        """记录 HTTP 错误请求/响应到日志文件。"""
        self._write_log(tag, payload, headers, response)

    def _log_http_exchange(
        self,
        tag: str,
        payload: Dict[str, Any],
        headers: Dict[str, str],
        response,
        response_content: str | None = None,
    ) -> None:
        """记录完整的请求/响应交换到日志文件（成功或失败）。

        Args:
            tag: 日志标签（如 "chat.completions"）
            payload: 请求体
            headers: 请求头
            response: HTTP 响应对象
            response_content: 响应正文（流式场景下需显式传入）
        """
        self._write_log(tag, payload, headers, response, response_content=response_content)

    def _write_log(
        self,
        tag: str,
        payload: Dict[str, Any],
        headers: Dict[str, str],
        response,
        response_content: str | None = None,
    ) -> None:
        """将 API 调用记录以 JSON 行格式写入 logs/deepseek-YYYYMMDD.log。

        API 密钥在写入前脱敏为 "Bearer ***"。
        """
        log_dir = Path(__file__).resolve().parents[2] / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / f"deepseek-{datetime.utcnow().strftime('%Y%m%d')}.log"

        # 脱敏：隐藏真实 API Key
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


# ============================================================
# 模块级工具函数
# ============================================================

def _trim_tool_args(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """截断消息中过长的工具调用参数以节省 token。

    在 followup 请求中，文档生成等技能的参数可能包含完整 Markdown 内容，
    这些内容不需要在 followup 中重复发送（模型已知），截断可大幅减少 token。

    Args:
        messages: 消息列表

    Returns:
        处理后的消息列表（浅拷贝）。
    """
    result = list(messages)
    for msg in result:
        tool_calls = msg.get("tool_calls", [])
        for tc in tool_calls:
            func = tc.get("function", {})
            args = func.get("arguments", "")
            if isinstance(args, str) and len(args) > MAX_TOOL_ARGS_IN_FOLLOWUP:
                func["arguments"] = (
                    args[:MAX_TOOL_ARGS_IN_FOLLOWUP]
                    + f'... [args truncated, {len(args)} chars total]'
                )
    return result


def load_system_prompt() -> str:
    """从 src/prompt/system.md 读取系统提示词模板。"""
    prompt_path = Path(__file__).parent.parent / "prompt" / "system.md"
    return prompt_path.read_text(encoding="utf-8").strip()


if __name__ == "__main__":
    model = Model()
    print(model.system_prompt)
