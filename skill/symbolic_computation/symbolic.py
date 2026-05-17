"""
Symbolic Computation Skill —— 基于 SymPy 进行符号计算。
"""
import sympy as sp


def skill_entry(payload: dict) -> str:
    """执行符号计算任务。"""
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
        # 解析表达式
        try:
            expr = sp.sympify(expression)
        except Exception:
            expr = eval(expression, {"x": x, "sp": sp, "sympy": sp,
                        "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
                        "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,
                        "pi": sp.pi, "E": sp.E, "oo": sp.oo})

        result = None
        result_latex = ""

        if task == "derivative" or task == "diff":
            order = extra.get("order", 1)
            result = sp.diff(expr, x, order)
            result_latex = sp.latex(result)
            return (
                f"【导数计算】\n"
                f"原函数: ${sp.latex(expr)}$\n"
                f"{order}阶导数: ${result_latex}$\n"
                f"简化结果: ${sp.latex(sp.simplify(result))}$"
            )

        elif task == "integral" or task == "integrate":
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

        elif task == "limit":
            point = extra.get("point", 0)
            direction = extra.get("direction", "")
            if direction == "+":
                result = sp.limit(expr, x, point, dir='+')
            elif direction == "-":
                result = sp.limit(expr, x, point, dir='-')
            else:
                result = sp.limit(expr, x, point)
            return (
                f"【极限计算】\n"
                f"表达式: ${sp.latex(expr)}$\n"
                f"趋向: x → {point}{direction}\n"
                f"结果: ${sp.latex(result)}$"
            )

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

        elif task == "matrix":
            # 期望 expression 是矩阵格式，如 "[[1,2],[3,4]]"
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

        elif task == "simplify" or task == "simplify":
            result = sp.simplify(expr)
            return (
                f"【表达式化简】\n"
                f"原表达式: ${sp.latex(expr)}$\n"
                f"化简结果: ${sp.latex(result)}$"
            )

        elif task == "expand":
            result = sp.expand(expr)
            return (
                f"【表达式展开】\n"
                f"原表达式: ${sp.latex(expr)}$\n"
                f"展开结果: ${sp.latex(result)}$"
            )

        elif task == "factor":
            result = sp.factor(expr)
            return (
                f"【因式分解】\n"
                f"原表达式: ${sp.latex(expr)}$\n"
                f"分解结果: ${sp.latex(result)}$"
            )

        else:
            # 自动尝试：先尝试求值，再尝试简化
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
