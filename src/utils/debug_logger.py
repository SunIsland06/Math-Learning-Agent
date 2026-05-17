"""
调试日志模块 —— 当 config/global.yml 中 debug: true 时启用。

以可读文本格式记录程序执行过程的关键信息：
- LLM 提示词/响应的摘要
- Skill 调用详情（参数/返回值）
- MCP 工具调用
- RAG 知识库引用
- 长期记忆读取

日志文件：logs/debug/debug-YYYYMMDD.log
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

_DEBUG_ENABLED = None
_LOG_FILE = None


def is_debug_enabled() -> bool:
    global _DEBUG_ENABLED
    if _DEBUG_ENABLED is not None:
        return _DEBUG_ENABLED
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
        from config.globalConfig import get_global_config
        _DEBUG_ENABLED = bool(getattr(get_global_config(), "debug", False))
    except Exception:
        _DEBUG_ENABLED = False
    return _DEBUG_ENABLED


def _get_log_path() -> Path:
    global _LOG_FILE
    if _LOG_FILE is not None:
        return _LOG_FILE
    log_dir = Path(__file__).resolve().parents[2] / "logs" / "debug"
    log_dir.mkdir(parents=True, exist_ok=True)
    _LOG_FILE = log_dir / f"debug-{datetime.utcnow().strftime('%Y%m%d')}.log"
    return _LOG_FILE


def _write(tag: str, lines: List[str]) -> None:
    """写入带时间戳和标签的文本行。"""
    if not is_debug_enabled():
        return
    ts = datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]
    try:
        with open(_get_log_path(), "a", encoding="utf-8") as f:
            f.write(f"\n{'='*70}\n")
            f.write(f"  [{ts}] {tag}\n")
            f.write(f"{'-'*70}\n")
            for line in lines:
                f.write(f"  {line}\n")
            f.write(f"{'='*70}\n")
    except Exception:
        pass


# ============================================================
# 公共 API
# ============================================================

def debug_log(tag: str, message: str) -> None:
    """写入单条短日志。"""
    if not is_debug_enabled():
        return
    ts = datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]
    try:
        with open(_get_log_path(), "a", encoding="utf-8") as f:
            f.write(f"  [{ts}] [{tag}] {message}\n")
    except Exception:
        pass


def log_prompt(prompt_type: str, messages: list, extra: Optional[Dict] = None) -> None:
    """记录发送给 LLM 的提示词摘要。"""
    if not is_debug_enabled():
        return
    lines = [f"类型: {prompt_type}", f"消息总数: {len(messages)}"]
    if extra:
        if extra.get("temperature"):
            lines.append(f"温度: {extra['temperature']}")
        if extra.get("tools_count"):
            lines.append(f"工具数: {extra['tools_count']}")
        if extra.get("enable_search"):
            lines.append("搜索: 已开启")
        if extra.get("enable_memory"):
            lines.append("记忆: 已开启")

    lines.append("")
    lines.append("--- 消息摘要 (最近8条) ---")
    for i, m in enumerate(messages[-8:]):
        role = m.get("role", "?")
        content = m.get("content", "")
        if isinstance(content, list):
            parts = [p.get("type", "?") for p in content]
            content = f"[多模态: {', '.join(parts)}]"
        elif isinstance(content, str):
            content = content[:200].replace("\n", "\\n")
        tc_list = m.get("tool_calls", [])
        if tc_list:
            tc_names = [tc.get("function", {}).get("name", "?") for tc in tc_list]
            content += f" [工具调用: {', '.join(tc_names)}]"
        lines.append(f"  [{i+1}] {role}: {content}")
    _write("LLM 请求", lines)


def log_response(prompt_type: str, content: str, reasoning_len: int = 0) -> None:
    """记录 LLM 响应。"""
    if not is_debug_enabled():
        return
    preview = content[:500].replace("\n", "\\n")
    lines = [
        f"类型: {prompt_type}",
        f"正文长度: {len(content)} 字符",
        f"推理长度: {reasoning_len} 字符",
        f"正文预览: {preview}...",
    ]
    _write("LLM 响应", lines)


def log_skill_call(name: str, arguments: str, result: str) -> None:
    """记录技能调用详情。"""
    if not is_debug_enabled():
        return
    args_preview = arguments[:500].replace("\n", "\\n")
    result_preview = result[:500].replace("\n", "\\n")
    lines = [
        f"技能名称: {name}",
        f"参数长度: {len(arguments)} 字符",
        f"参数内容: {args_preview}",
        f"---",
        f"结果长度: {len(result)} 字符",
        f"结果预览: {result_preview}",
    ]
    _write(f"Skill 调用 → {name}", lines)


def log_mcp_call(tool_name: str, args: str, result_len: int) -> None:
    """记录 MCP 工具调用。"""
    if not is_debug_enabled():
        return
    lines = [
        f"MCP 工具: {tool_name}",
        f"参数: {args[:300]}",
        f"结果长度: {result_len} 字符",
    ]
    _write(f"MCP 调用 → {tool_name}", lines)


def log_rag_retrieve(query: str, sources: list, context_len: int) -> None:
    """记录 RAG 知识库检索。"""
    if not is_debug_enabled():
        return
    lines = [
        f"检索查询: {query[:200]}",
        f"匹配来源数: {len(sources)}",
    ]
    for i, s in enumerate(sources, 1):
        lines.append(f"  来源{i}: {s}")
    lines.append(f"上下文总长: {context_len} 字符")
    if context_len > 0:
        lines.append("→ RAG 上下文已注入到 LLM 请求")
    else:
        lines.append("→ 未检索到相关知识库内容")
    _write("RAG 知识库检索", lines)


def log_memory_read(username: str, query: str, memory_count: int) -> None:
    """记录长期记忆读取。"""
    if not is_debug_enabled():
        return
    lines = [
        f"用户: {username}",
        f"查询: {query[:200]}",
        f"匹配记忆数: {memory_count}",
    ]
    if memory_count > 0:
        lines.append("→ 记忆上下文已注入到 LLM 请求")
    else:
        lines.append("→ 无相关历史记忆")
    _write("长期记忆读取", lines)
