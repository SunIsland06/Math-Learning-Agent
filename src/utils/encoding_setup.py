"""
编码初始化工具 —— 在 Windows 系统上强制使用 UTF-8，解决 GBK 控制台乱码问题。

使用方式（在模块顶部调用）：
    from utils.encoding_setup import setup_windows_utf8
    setup_windows_utf8()
"""

import sys
import os


def setup_windows_utf8():
    """在 Windows 平台上将 stdout/stderr 重配置为 UTF-8。

    解决 Windows PowerShell / CMD 下 Python 输出中文时
    因 GBK 编码导致的乱码或 UnicodeEncodeError。
    """
    if sys.platform != "win32":
        return

    # 方法1：Python 3.7+ 的 reconfigure API
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    # 方法2：环境变量（影响子进程和 C 扩展）
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    os.environ.setdefault("PYTHONUTF8", "1")

    # 方法3：确保 requests/httpx 等库使用 UTF-8 输出
    if hasattr(sys, "getdefaultencoding") and sys.getdefaultencoding().lower() != "utf-8":
        try:
            sys.setdefaultencoding("utf-8")
        except AttributeError:
            pass
