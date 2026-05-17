"""
Code Execution Skill —— 安全沙箱执行 Python 代码，用于数学计算辅助。
"""
import io
import sys
import traceback
import numpy as np


# 允许的安全内置函数和模块
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
    """执行 Python 代码并返回捕获的输出。"""
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

        # 执行代码
        exec(code.strip(), safe_globals, {})
        output = sys.stdout.getvalue()

        if output.strip():
            return f"【代码执行结果】\n```\n{output.strip()}\n```"
        return "【代码执行完成】代码已执行，无标准输出。"
    except Exception as e:
        tb = traceback.format_exc()
        return f"【代码执行错误】\n```\n{tb}\n```"
    finally:
        sys.stdout = old_stdout
