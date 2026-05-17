"""
MCP 客户端管理器 —— 管理 MCP 服务器生命周期，为 Agent 提供工具发现和执行。

架构：
- 在后台守护线程中运行 asyncio 事件循环
- 通过 stdio 子进程方式连接本地 MCP 服务器（遵循 Model Context Protocol）
- 对外暴露同步接口（build_tools / execute_tool），供 model.py 直接调用

当前支持的 MCP 服务：
- web_search: 联网搜索引擎（DuckDuckGo + 网页内容提取）

使用方式：
    from mcp_services.mcp_manager import get_mcp_manager
    mgr = get_mcp_manager()
    mgr.register_server("web_search", "web_search_server.py")
    mgr.start()
"""

import asyncio
import json
import os
import sys
import threading
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession


def _server_path(name: str) -> str:
    """获取 MCP 服务器脚本的绝对路径（相对于当前文件所在目录）。"""
    base = Path(__file__).resolve().parent
    return str(base / name)


class MCPManager:
    """MCP 管理器 —— 桥接同步 Flask 应用与异步 MCP 协议。

    核心职责：
    1. 在后台线程启动 asyncio 事件循环
    2. 通过 stdio 连接本地 MCP 服务器并完成协议初始化
    3. 发现并缓存远程工具列表
    4. 提供同步工具执行接口（跨线程调度到事件循环）
    """

    def __init__(self):
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._thread: Optional[threading.Thread] = None
        self._session: Optional[ClientSession] = None
        self._ready = False
        self._server_scripts: List[str] = []
        self._tools: List[Dict[str, Any]] = []
        self._init_event = threading.Event()  # 初始化完成信号量
        self._shutdown_event: Optional[asyncio.Event] = None

    # ============================================================
    # 公共 API
    # ============================================================

    def register_server(self, name: str, script: str, description: str = "") -> None:
        """注册一个 MCP 服务器（须在 start() 前调用）。

        Args:
            name: 服务器名称（用于日志标识）
            script: 服务器脚本文件名（相对于 src/mcp_services/）
            description: 服务描述
        """
        self._server_scripts.append(script)

    def start(self) -> None:
        """启动 MCP 管理器 —— 在后台守护线程中建立与所有 MCP 服务器的连接。

        设置 30 秒超时等待初始化完成，超时后打印警告但不阻塞应用启动。
        """
        if not self._server_scripts:
            return
        self._init_event.clear()
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

        if not self._init_event.wait(timeout=30):
            print("[MCP] MCP 管理器启动超时（30s）")

    def stop(self) -> None:
        """关闭所有 MCP 连接并停止后台线程。"""
        if self._shutdown_event and self._loop and self._loop.is_running():
            asyncio.run_coroutine_threadsafe(self._signal_shutdown(), self._loop)
        if self._loop:
            self._loop.call_soon_threadsafe(self._loop.stop)

    def is_ready(self) -> bool:
        """检查 MCP 管理器是否已就绪（连接建立且工具已发现）。"""
        return self._ready

    def build_tools(self) -> List[Dict[str, Any]]:
        """获取 MCP 服务器提供的 OpenAI 格式工具定义列表。"""
        return list(self._tools)

    def execute_tool(self, name: str, arguments: str) -> str:
        """同步执行一个 MCP 工具调用。

        内部通过 asyncio.run_coroutine_threadsafe 将执行请求
        调度到后台事件循环，并阻塞等待结果。

        Args:
            name: 工具名称
            arguments: JSON 格式参数字符串

        Returns:
            工具执行结果字符串。
        """
        if not self._ready or not self._loop:
            return "MCP 服务未就绪"
        try:
            args_dict = json.loads(arguments) if arguments else {}
        except json.JSONDecodeError:
            args_dict = {"input": arguments}

        future = asyncio.run_coroutine_threadsafe(
            self._call_tool(name, args_dict), self._loop
        )
        try:
            return future.result(timeout=120)
        except Exception as e:
            return f"MCP 工具调用失败: {e}"

    # ============================================================
    # 后台线程与事件循环
    # ============================================================

    def _run_loop(self) -> None:
        """后台线程入口 —— 设置事件循环并运行直到 stop() 被调用。"""
        asyncio.set_event_loop(self._loop)
        self._loop.create_task(self._session_loop())
        self._loop.run_forever()

    async def _session_loop(self) -> None:
        """MCP 会话主协程：连接 → 发现工具 → 保持活跃 → 优雅关闭。

        当前支持单服务器连接，多服务器扩展只需遍历 _server_scripts。
        """
        self._shutdown_event = asyncio.Event()

        for script in self._server_scripts:
            server_path = _server_path(script)
            env = os.environ.copy()
            env.setdefault("PYTHONIOENCODING", "utf-8")
            params = StdioServerParameters(
                command=sys.executable,
                args=[server_path],
                env=env,
            )
            try:
                # 使用 async with 管理 MCP 客户端生命周期
                async with stdio_client(params) as (read, write):
                    async with ClientSession(read, write) as session:
                        self._session = session
                        # MCP 协议初始化握手
                        await session.initialize()
                        # 发现远程工具
                        result = await session.list_tools()
                        self._tools.clear()
                        for tool in result.tools:
                            self._tools.append({
                                "type": "function",
                                "function": {
                                    "name": tool.name,
                                    "description": tool.description or f"工具: {tool.name}",
                                    "parameters": tool.inputSchema if tool.inputSchema else {
                                        "type": "object",
                                        "properties": {
                                            "query": {"type": "string", "description": "搜索关键词"},
                                        },
                                        "required": ["query"],
                                    },
                                },
                            })
                        print(
                            f"[MCP] 服务器 '{script}' 连接成功，"
                            f"发现 {len(self._tools)} 个工具: "
                            f"{[t['function']['name'] for t in self._tools]}"
                        )
                        self._ready = True
                        self._init_event.set()

                        # 等待关闭信号（期间 _call_tool 可正常使用 session）
                        await self._shutdown_event.wait()
            except Exception as e:
                print(f"[MCP] 服务器 '{script}' 连接失败: {e}")
                import traceback
                traceback.print_exc()
            finally:
                self._ready = False
                self._session = None

    async def _call_tool(self, name: str, args: Dict[str, Any]) -> str:
        """在事件循环内异步执行工具调用。

        Args:
            name: 工具名称
            args: 参数字典

        Returns:
            工具执行结果文本。
        """
        if not self._session:
            return "MCP 会话未建立"
        try:
            result = await self._session.call_tool(name, args)
            if result.content:
                parts = []
                for c in result.content:
                    if hasattr(c, "text"):
                        parts.append(c.text)
                return "\n".join(parts) if parts else str(result.content)
            return ""
        except Exception as e:
            return f"MCP 工具执行错误: {e}"

    async def _signal_shutdown(self) -> None:
        """触发关闭信号，通知 _session_loop 退出。"""
        if self._shutdown_event:
            self._shutdown_event.set()


# ============================================================
# 全局单例
# ============================================================

_mcp_manager: Optional[MCPManager] = None


def get_mcp_manager() -> MCPManager:
    """获取 MCPManager 全局单例实例（延迟初始化）。"""
    global _mcp_manager
    if _mcp_manager is None:
        _mcp_manager = MCPManager()
    return _mcp_manager
