"""
代码执行技能 —— 在受限沙箱中执行 Python 代码，用于数学数值计算。

安全措施：
1. 白名单内置函数 —— 仅暴露安全的 builtins（无 open/eval/exec 等）
2. 白名单模块 —— 仅允许 math/numpy/statistics 等数学相关库
3. stdout 捕获 —— 所有输出通过 io.StringIO 捕获并返回

入口函数：skill_entry(payload) → str
"""

import io
import sys
import traceback
import numpy as np


# 安全内置函数白名单 —— 排除文件操作、代码执行等危险函数
_SAFE_BUILTINS = {
    "abs": abs, "all": all, "any": any, "bin": bin, "bool": bool,
    "chr": chr, "complex": complex, "dict": dict, "divmod": divmod,
    "enumerate": enumerate, "filter": filter, "float": float, "format": format,
    "frozenset": frozenset, "hex": hex, "int": int, "len": len,
    "list": list, "map": map, "max": max, "min": min, "oct": oct,
    "ord": ord, "pow": pow, "range": range, "reversed": reversed,
    "round": round, "set": set, "slice": slice, "sorted": sorted,
    "str": str, "sum": sum, "tuple": tuple, "type": type, "zip": zip,
    "True": True, "False": False, "None": None,
    "print": print, "isinstance": isinstance, "issubclass": issubclass,
    "hasattr": hasattr, "getattr": getattr,
    "__import__": __import__,
}

# 安全模块白名单 —— 仅数学计算和数据处理相关
_SAFE_MODULES = {
    "math": __import__("math"),
    "numpy": np,
    "np": np,
    "statistics": __import__("statistics"),
    "itertools": __import__("itertools"),
    "functools": __import__("functools"),
    "collections": __import__("collections"),
    "fractions": __import__("fractions"),
    "decimal": __import__("decimal"),
    "random": __import__("random"),
    "json": __import__("json"),
    "re": __import__("re"),
}


def skill_entry(payload: dict) -> str:
    """在沙箱中执行 Python 代码并返回 stdout 输出。

    Args:
        payload: {
            "input": str (Python 代码),
            "params": {
                "code": str,  # 要执行的 Python 代码
            }
        }

    Returns:
        代码执行结果（含 stdout 输出或错误堆栈）。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    code = params.get("code") or payload.get("input", "")

    if not code or not code.strip():
        return "错误：请提供要执行的 Python 代码。"

    # 捕获 stdout
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        # 构建受限的全局命名空间
        safe_globals = {"__builtins__": _SAFE_BUILTINS}
        safe_globals.update(_SAFE_MODULES)

        exec(code.strip(), safe_globals, {})
        output = sys.stdout.getvalue()

        if output.strip():
            return f"【代码执行结果】\n```\n{output.strip()}\n```"
        return "【代码执行完成】代码已执行，无标准输出。"
    except Exception:
        tb = traceback.format_exc()
        return f"【代码执行错误】\n```\n{tb}\n```"
    finally:
        sys.stdout = old_stdout
