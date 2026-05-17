"""
调试日志模块 —— 当 config/global.yml 中 DEBUG=true 时启用。

记录的关键信息：
- 提示词输入输出（截断显示）
- 技能调用情况（名称、参数、结果摘要）
- MCP 工具调用
- 知识库引用（来源、匹配分数）
- 长期记忆读取

使用方式：
    from utils.debug_logger import debug_log, is_debug_enabled
    if is_debug_enabled():
        debug_log("tag", {"key": "value"})
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

_DEBUG_ENABLED = None
_LOG_DIR = None


def is_debug_enabled() -> bool:
    """检查是否开启了 DEBUG 模式（从 global.yml 读取）。"""
    global _DEBUG_ENABLED
    if _DEBUG_ENABLED is not None:
        return _DEBUG_ENABLED

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
        from config.globalConfig import get_global_config
        cfg = get_global_config()
        _DEBUG_ENABLED = getattr(cfg, "debug", False) or False
    except Exception:
        _DEBUG_ENABLED = False
    return _DEBUG_ENABLED


def _get_log_dir() -> Path:
    """获取调试日志目录。"""
    global _LOG_DIR
    if _LOG_DIR is not None:
        return _LOG_DIR
    _LOG_DIR = Path(__file__).resolve().parents[2] / "logs" / "debug"
    _LOG_DIR.mkdir(parents=True, exist_ok=True)
    return _LOG_DIR


def debug_log(tag: str, data: Dict[str, Any], max_str_len: int = 2000) -> None:
    """写入一条调试日志。

    Args:
        tag: 日志标签（如 "prompt_in", "skill_call", "rag_retrieve"）
        data: 要记录的键值对数据
        max_str_len: 字符串值的最大长度（超出截断）
    """
    if not is_debug_enabled():
        return

    log_file = _get_log_dir() / f"debug-{datetime.utcnow().strftime('%Y%m%d')}.log"

    # 截断过长的字符串值
    safe_data = {}
    for k, v in data.items():
        if isinstance(v, str) and len(v) > max_str_len:
            safe_data[k] = v[:max_str_len] + f"... [truncated, total {len(v)} chars]"
        elif isinstance(v, dict):
            safe_data[k] = _truncate_dict(v, max_str_len)
        elif isinstance(v, list):
            safe_data[k] = _truncate_list(v, max_str_len)
        else:
            safe_data[k] = v

    record = {
        "time": datetime.utcnow().isoformat() + "Z",
        "tag": tag,
        "data": safe_data,
    }

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _truncate_dict(d: dict, max_len: int) -> dict:
    """递归截断字典中的长字符串。"""
    result = {}
    for k, v in d.items():
        if isinstance(v, str) and len(v) > max_len:
            result[k] = v[:max_len] + f"... [{len(v)} chars]"
        elif isinstance(v, dict):
            result[k] = _truncate_dict(v, max_len)
        elif isinstance(v, list):
            result[k] = _truncate_list(v, max_len)
        else:
            result[k] = v
    return result


def _truncate_list(lst: list, max_len: int) -> list:
    """递归截断列表中的长字符串。"""
    result = []
    for item in lst:
        if isinstance(item, str) and len(item) > max_len:
            result.append(item[:max_len] + f"... [{len(item)} chars]")
        elif isinstance(item, dict):
            result.append(_truncate_dict(item, max_len))
        elif isinstance(item, list):
            result.append(_truncate_list(item, max_len))
        else:
            result.append(item)
    return result


def log_prompt(prompt_type: str, messages: list, extra: Optional[Dict] = None) -> None:
    """记录 LLM 提示词输入。

    Args:
        prompt_type: "initial" 或 "followup"
        messages: 发送给 LLM 的消息列表
        extra: 额外参数（temperature, tools 等）
    """
    if not is_debug_enabled():
        return

    summary = []
    for m in messages[-8:]:  # 仅记录最近8条
        role = m.get("role", "?")
        content = m.get("content", "")
        if isinstance(content, list):
            content = "[multimodal: " + str(len(content)) + " parts]"
        elif isinstance(content, str) and len(content) > 300:
            content = content[:300] + "..."
        tool_calls = m.get("tool_calls", [])
        tc_summary = []
        for tc in tool_calls:
            fn = tc.get("function", {})
            tc_summary.append({
                "name": fn.get("name", "?"),
                "args_len": len(fn.get("arguments", "")),
            })
        entry = {"role": role}
        if content:
            entry["content_preview"] = content
        if tc_summary:
            entry["tool_calls"] = tc_summary
        summary.append(entry)

    data = {
        "prompt_type": prompt_type,
        "total_messages": len(messages),
        "messages_summary": summary,
    }
    if extra:
        data["extra"] = {k: v for k, v in extra.items() if k != "messages"}
    debug_log("prompt_in", data)


def log_response(prompt_type: str, content: str, reasoning_len: int = 0) -> None:
    """记录 LLM 响应输出。

    Args:
        prompt_type: "initial" 或 "followup"
        content: LLM 返回的文本内容
        reasoning_len: 思考内容长度
    """
    if not is_debug_enabled():
        return
    preview = content[:500] + "..." if len(content) > 500 else content
    debug_log("llm_response", {
        "prompt_type": prompt_type,
        "content_length": len(content),
        "content_preview": preview,
        "reasoning_length": reasoning_len,
    })


def log_skill_call(name: str, args: str, result: str) -> None:
    """记录技能调用。

    Args:
        name: 技能名称
        args: 调用参数
        result: 返回结果
    """
    if not is_debug_enabled():
        return
    debug_log("skill_call", {
        "skill_name": name,
        "args_length": len(args),
        "args_preview": args[:300] if len(args) > 300 else args,
        "result_length": len(result),
        "result_preview": result[:300] if len(result) > 300 else result,
    })


def log_rag_retrieve(query: str, sources: list, context_len: int) -> None:
    """记录 RAG 知识库检索。

    Args:
        query: 检索查询
        sources: 匹配来源列表
        context_len: 检索到的上下文字符数
    """
    if not is_debug_enabled():
        return
    debug_log("rag_retrieve", {
        "query_preview": query[:200] if len(query) > 200 else query,
        "sources": sources[:5],
        "context_length": context_len,
    })


def log_memory_read(username: str, query: str, memory_count: int) -> None:
    """记录长期记忆读取。

    Args:
        username: 用户名
        query: 查询文本
        memory_count: 检索到的记忆数量
    """
    if not is_debug_enabled():
        return
    debug_log("memory_read", {
        "username": username,
        "query_preview": query[:200] if len(query) > 200 else query,
        "memories_found": memory_count,
    })


def log_mcp_call(tool_name: str, args: str, result_len: int) -> None:
    """记录 MCP 工具调用。

    Args:
        tool_name: 工具名称
        args: 调用参数
        result_len: 结果长度
    """
    if not is_debug_enabled():
        return
    debug_log("mcp_call", {
        "tool_name": tool_name,
        "args_preview": args[:200] if len(args) > 200 else args,
        "result_length": result_len,
    })
