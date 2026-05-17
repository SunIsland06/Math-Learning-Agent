"""
符号计算技能 —— 基于 SymPy 提供数学符号运算能力。

支持的计算类型：
- derivative/diff: 求导（可指定阶数）
- integral/integrate: 积分（定积分/不定积分）
- limit: 极限（可指定方向和趋近点）
- solve: 方程求解
- matrix: 矩阵运算（行列式/逆矩阵/特征值/秩）
- series: 级数展开
- simplify: 表达式化简
- expand: 表达式展开
- factor: 因式分解

入口函数：skill_entry(payload) → str
"""

import sympy as sp


def skill_entry(payload: dict) -> str:
    """执行符号计算任务并返回格式化结果。

    Args:
        payload: {
            "input": str (数学表达式),
            "params": {
                "task": str,          # 计算类型
                "expression": str,    # 表达式
                "variable": str,      # 变量名（默认 "x"）
                "extra": {            # 额外参数（阶数/区间等）
                    "order": int,
                    "lower": number,
                    "upper": number,
                    "point": number,
                    "direction": str,
                    "op": str,
                }
            }
        }

    Returns:
        包含 LaTeX 公式的 Markdown 格式结果字符串。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    input_text = payload.get("input", "")

    task = params.get("task", "")
    expression = params.get("expression") or input_text or ""
    variable = params.get("variable", "x")
    extra = params.get("extra", {})

    if not expression.strip():
        return "错误：请提供数学表达式。"

    try:
        x = sp.Symbol(variable)
        # 解析表达式：优先 SymPy sympify，失败时回退到 eval
        try:
            expr = sp.sympify(expression)
        except Exception:
            expr = eval(expression, {
                "x": x, "sp": sp, "sympy": sp,
                "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
                "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,
                "pi": sp.pi, "E": sp.E, "oo": sp.oo,
            })

        # ---- 求导 ----
        if task in ("derivative", "diff"):
            order = extra.get("order", 1)
            result = sp.diff(expr, x, order)
            return (
                f"【导数计算】\n"
                f"原函数: ${sp.latex(expr)}$\n"
                f"{order}阶导数: ${sp.latex(result)}$\n"
                f"简化结果: ${sp.latex(sp.simplify(result))}$"
            )

        # ---- 积分 ----
        elif task in ("integral", "integrate"):
            lower = extra.get("lower")
            upper = extra.get("upper")
            if lower is not None and upper is not None:
                result = sp.integrate(expr, (x, lower, upper))
                return (
                    f"【定积分计算】\n"
                    f"被积函数: ${sp.latex(expr)}$\n"
                    f"积分区间: [{sp.latex(lower)}, {sp.latex(upper)}]\n"
                    f"结果: ${sp.latex(result)}$"
                )
            else:
                result = sp.integrate(expr, x)
                return (
                    f"【不定积分计算】\n"
                    f"被积函数: ${sp.latex(expr)}$\n"
                    f"原函数: ${sp.latex(result)} + C$"
                )

        # ---- 极限 ----
        elif task == "limit":
            point = extra.get("point", 0)
            direction = extra.get("direction", "")
            if direction == "+":
                result = sp.limit(expr, x, point, dir="+")
            elif direction == "-":
                result = sp.limit(expr, x, point, dir="-")
            else:
                result = sp.limit(expr, x, point)
            return (
                f"【极限计算】\n"
                f"表达式: ${sp.latex(expr)}$\n"
                f"趋向: x → {point}{direction}\n"
                f"结果: ${sp.latex(result)}$"
            )

        # ---- 方程求解 ----
        elif task == "solve":
            rhs = extra.get("rhs", 0)
            if rhs != 0:
                eq = sp.Eq(expr, rhs)
            else:
                eq = expr
            result = sp.solve(eq, x)
            return (
                f"【方程求解】\n"
                f"方程: ${sp.latex(eq)} = 0$\n"
                f"解: ${sp.latex(result)}$"
            )

        # ---- 矩阵运算 ----
        elif task == "matrix":
            M = sp.Matrix(eval(expression))
            op = extra.get("op", "det")
            if op == "det":
                result = M.det()
            elif op == "inv":
                result = M.inv()
            elif op == "eigenvals":
                result = M.eigenvals()
            elif op == "eigenvects":
                result = M.eigenvects()
            elif op == "rank":
                result = M.rank()
            else:
                result = M
            return (
                f"【矩阵运算】\n"
                f"矩阵: ${sp.latex(M)}$\n"
                f"操作: {op}\n"
                f"结果: ${sp.latex(result)}$"
            )

        # ---- 级数展开 ----
        elif task == "series":
            n = extra.get("n", 6)
            point = extra.get("point", 0)
            result = sp.series(expr, x, point, n)
            result_removed = result.removeO()
            return (
                f"【级数展开】\n"
                f"表达式: ${sp.latex(expr)}$\n"
                f"在 x={point} 处展开至 {n} 阶:\n"
                f"${sp.latex(result)}$\n"
                f"展开项: ${sp.latex(result_removed)}$"
            )

        # ---- 化简 ----
        elif task in ("simplify",):
            result = sp.simplify(expr)
            return (
                f"【表达式化简】\n"
                f"原表达式: ${sp.latex(expr)}$\n"
                f"化简结果: ${sp.latex(result)}$"
            )

        # ---- 展开 ----
        elif task == "expand":
            result = sp.expand(expr)
            return (
                f"【表达式展开】\n"
                f"原表达式: ${sp.latex(expr)}$\n"
                f"展开结果: ${sp.latex(result)}$"
            )

        # ---- 因式分解 ----
        elif task == "factor":
            result = sp.factor(expr)
            return (
                f"【因式分解】\n"
                f"原表达式: ${sp.latex(expr)}$\n"
                f"分解结果: ${sp.latex(result)}$"
            )

        # ---- 自动模式：先数值求值再符号简化 ----
        else:
            try:
                result = sp.N(expr)
                if result.is_number:
                    return (
                        f"【数值计算】\n"
                        f"表达式: ${sp.latex(expr)}$\n"
                        f"数值结果: {result}"
                    )
            except Exception:
                pass

            result = sp.simplify(expr)
            return (
                f"【符号计算】\n"
                f"表达式: ${sp.latex(expr)}$\n"
                f"结果: ${sp.latex(result)}$"
            )

    except Exception as e:
        return f"【符号计算错误】无法处理表达式「{expression}」: {e}"
