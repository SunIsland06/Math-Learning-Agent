"""
MCP Web Search Server —— 提供 web_search 工具的本地 MCP 服务。

功能：
1. 通过 DuckDuckGo 搜索引擎获取前 10 个搜索结果
2. 异步获取前 3 个网页的正文内容（HTML → 纯文本）
3. 通过 stdio 传输，遵循 Model Context Protocol 标准

启动方式：由 MCPManager 作为子进程自动管理，无需手动启动。
"""

import re
import sys
from urllib.parse import urlparse

# Windows 下强制 UTF-8 编码，避免特殊字符（如 ²）导致 GBK 崩溃
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from ddgs import DDGS
from mcp.server.fastmcp import FastMCP
import httpx

# ============================================================
# HTML 清洗 —— 将网页 HTML 转为纯文本
# ============================================================

_RE_SCRIPT = re.compile(r"<script[^>]*>[\s\S]*?</script>", re.IGNORECASE)
_RE_STYLE = re.compile(r"<style[^>]*>[\s\S]*?</style>", re.IGNORECASE)
_RE_TAG = re.compile(r"<[^>]+>")
_RE_SPACE = re.compile(r"\s{2,}")


def _extract_text(html: str, max_chars: int = 3000) -> str:
    """从 HTML 中提取纯文本内容。

    依次移除 <script>、<style> 标签，剥离所有 HTML 标签，
    压缩多余空白，截取前 max_chars 个字符。

    Args:
        html: 原始 HTML 文本
        max_chars: 最大返回字符数

    Returns:
        清洗后的纯文本字符串。
    """
    text = _RE_SCRIPT.sub(" ", html)
    text = _RE_STYLE.sub(" ", text)
    text = _RE_TAG.sub(" ", text)
    text = _RE_SPACE.sub(" ", text)
    text = text.strip()
    if len(text) > max_chars:
        text = text[:max_chars] + "..."
    return text


def _is_valid_url(url: str) -> bool:
    """验证 URL 是否合法（仅允许 http/https 协议）。"""
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False


async def _fetch_page(url: str, timeout: float = 8.0) -> str:
    """异步获取网页内容并提取纯文本。

    Args:
        url: 网页 URL
        timeout: 请求超时秒数

    Returns:
        提取的纯文本内容，失败返回空字符串。
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            resp = await client.get(url, headers=headers)
            resp.raise_for_status()
            return _extract_text(resp.text)
    except Exception:
        return ""


# ============================================================
# FastMCP 服务器定义
# ============================================================

mcp = FastMCP("web-search")


@mcp.tool()
async def web_search(query: str) -> str:
    """联网搜索工具 —— 搜索互联网获取最新信息。

    用法：当需要查找当前事件、最新资料、或教材中未覆盖的知识时调用。
    参数：query — 搜索关键词。
    返回：前 10 个搜索结果（含标题、URL、摘要），以及前 3 个网页的正文内容。

    Args:
        query: 用户搜索关键词

    Returns:
        格式化的搜索结果文本（Markdown 兼容）。
    """
    if not query or not query.strip():
        return "错误：请提供搜索关键词。"

    query = query.strip()
    results_parts = [f"【联网搜索结果】关键词：「{query}」\n"]

    # 1) DuckDuckGo 搜索（auto 模式自动选择可用引擎）
    try:
        with DDGS(timeout=15) as ddgs:
            search_results = list(ddgs.text(query, max_results=10))
    except Exception as e:
        return f"搜索失败：{e}"

    if not search_results:
        return f"未找到与「{query}」相关的结果，建议换个关键词重试。"

    # 2) 搜索结果列表（前 10 条）
    results_parts.append("─" * 40)
    results_parts.append("搜索结果列表：\n")
    for i, r in enumerate(search_results, 1):
        title = r.get("title", "无标题")
        href = r.get("href", "")
        body = r.get("body", "")
        results_parts.append(f"{i}. {title}")
        results_parts.append(f"   URL: {href}")
        results_parts.append(f"   摘要: {body}")
        results_parts.append("")

    # 3) 获取前 3 个有效网页的正文内容
    results_parts.append("─" * 40)
    results_parts.append("网页正文（前 3 个）：\n")

    fetched_count = 0
    for r in search_results:
        if fetched_count >= 3:
            break
        href = r.get("href", "")
        if not _is_valid_url(href):
            continue
        title = r.get("title", "无标题")
        content = await _fetch_page(href)
        if content:
            fetched_count += 1
            results_parts.append(f"【{fetched_count}】{title}")
            results_parts.append(f"来源: {href}")
            results_parts.append(content[:2000])
            results_parts.append("")

    results_parts.append("─" * 40)
    results_parts.append(
        f"共搜索到 {len(search_results)} 条结果，已提取 {fetched_count} 个网页正文。"
    )

    return "\n".join(results_parts)


if __name__ == "__main__":
    mcp.run()
