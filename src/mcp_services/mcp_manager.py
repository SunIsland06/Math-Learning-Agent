"""
MCP 客户端管理器 —— 管理 MCP 服务器生命周期，为 Agent 提供工具发现和执行。
通过 stdio 子进程方式连接本地 MCP 服务器。
"""
import asyncio
import json
import sys
import threading
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession


def _server_path(name: str) -> str:
    base = Path(__file__).resolve().parent
    return str(base / name)


class MCPManager:
    """
    MCP 管理器 —— 在后台线程中运行 asyncio 事件循环，
    通过 stdio 连接本地 MCP 服务器，并对外暴露同步接口。
    """

    def __init__(self):
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._thread: Optional[threading.Thread] = None
        self._session: Optional[ClientSession] = None
        self._ready = False
        self._server_scripts: List[str] = []
        self._tools: List[Dict[str, Any]] = []
        self._init_event = threading.Event()  # 初始化完成信号
        self._shutdown_event: Optional[asyncio.Event] = None

    # ---- 公共 API ----

    def register_server(self, name: str, script: str, description: str = "") -> None:
        """注册一个 MCP 服务器（须在 start() 前调用）。"""
        self._server_scripts.append(script)

    def start(self) -> None:
        """启动 MCP 管理器：在后台线程建立与所有 MCP 服务器的连接。"""
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
        return self._ready

    def build_tools(self) -> List[Dict[str, Any]]:
        return list(self._tools)

    def execute_tool(self, name: str, arguments: str) -> str:
        """同步执行一个 MCP 工具调用。"""
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

    # ---- 内部实现 ----

    def _run_loop(self) -> None:
        asyncio.set_event_loop(self._loop)
        # 启动会话主协程（内部使用 async with，保持连接直到 shutdown）
        self._loop.create_task(self._session_loop())
        self._loop.run_forever()

    async def _session_loop(self) -> None:
        """主协程：建立连接 → 发现工具 → 保持活跃 → 优雅关闭。"""
        self._shutdown_event = asyncio.Event()

        # 连接所有服务器（当前仅支持单服务器，多服务器可扩展）
        for script in self._server_scripts:
            server_path = _server_path(script)
            params = StdioServerParameters(
                command=sys.executable,
                args=[server_path],
                env=None,
            )
            try:
                async with stdio_client(params) as (read, write):
                    async with ClientSession(read, write) as session:
                        self._session = session
                        await session.initialize()
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
                                            "query": {"type": "string", "description": "搜索关键词"}
                                        },
                                        "required": ["query"],
                                    },
                                },
                            })
                        print(f"[MCP] 服务器 '{script}' 连接成功，发现 {len(self._tools)} 个工具: "
                              f"{[t['function']['name'] for t in self._tools]}")
                        self._ready = True
                        self._init_event.set()

                        # 等待关闭信号，期间 _call_tool 可正常使用 session
                        await self._shutdown_event.wait()
            except Exception as e:
                print(f"[MCP] 服务器 '{script}' 连接失败: {e}")
                import traceback
                traceback.print_exc()
            finally:
                self._ready = False
                self._session = None

    async def _call_tool(self, name: str, args: Dict[str, Any]) -> str:
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
        if self._shutdown_event:
            self._shutdown_event.set()


# 全局单例
_mcp_manager: Optional[MCPManager] = None


def get_mcp_manager() -> MCPManager:
    global _mcp_manager
    if _mcp_manager is None:
        _mcp_manager = MCPManager()
    return _mcp_manager
