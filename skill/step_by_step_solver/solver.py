"""
Step-by-Step Solver Skill —— 生成数学题目的分步解题过程。
"""
import re
import sympy as sp


def _preprocess_math(problem: str) -> str:
    """预处理数学表达式，将常见数学语法转为 SymPy 可解析的格式。"""
    text = problem.strip()
    # 去掉前置命令词
    text = re.sub(r"^(solve|calculate|find|compute|evaluate|determine|verify|simplify|expand|factor|differentiate|integrate)\s+",
                  "", text, flags=re.IGNORECASE)
    # 将 ^ 替换为 ** (幂运算)
    text = re.sub(r"(\w+|\))\s*\^\s*(\w+|\(|-)", r"\1**\2", text)
    # 处理隐式乘法：数字后接字母，如 5x → 5*x
    text = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", text)
    # 处理 )数字 或 字母( 等
    text = re.sub(r"\)(\d)", r")*\1", text)
    # 处理隐式乘法：数字后接 ( 如 2(x+1) → 2*(x+1)
    text = re.sub(r"(\d)\(", r"\1*(", text)
    return text


def _try_sympy_steps(problem: str) -> str:
    """尝试用 SymPy 自动解析并生成解题步骤。"""
    x = sp.Symbol("x")

    # 预处理数学表达式
    processed = _preprocess_math(problem)

    # 尝试识别问题类型并生成步骤
    steps = []
    problem_lower = problem.lower()

    try:
        # 尝试解析为等式
        if "=" in processed:
            parts = processed.split("=")
            left = sp.sympify(parts[0].strip())
            right = sp.sympify(parts[1].strip())
            eq = sp.Eq(left, right)

            steps.append(f"**步骤 1** — 建立方程：${sp.latex(eq)}$")

            try:
                solutions = sp.solve(eq, x)
                steps.append(f"**步骤 2** — 移项整理为标准形式")
                steps.append(f"**步骤 3** — 求解方程")
                if solutions:
                    steps.append(f"**步骤 4** — 得出解：${sp.latex(solutions)}$")
                    steps.append(f"\n答案：$x = {sp.latex(solutions)}$")
                else:
                    steps.append("该方程无实数解。")
            except Exception:
                steps.append("**步骤 2** — 方程需进一步分析")
        else:
            # 尝试作为表达式
            expr = sp.sympify(processed)

            # 导数
            deriv = sp.diff(expr, x)
            if deriv != 0:
                steps.append(f"**求导过程：**")
                steps.append(f"1. 原函数：$f(x) = {sp.latex(expr)}$")
                steps.append(f"2. 求导：$f'(x) = {sp.latex(deriv)}$")
                simplified = sp.simplify(deriv)
                if simplified != deriv:
                    steps.append(f"3. 化简：$f'(x) = {sp.latex(simplified)}$")

            # 积分
            integral = sp.integrate(expr, x)
            if integral != expr * x:
                steps.append(f"\n**积分过程：**")
                steps.append(f"1. 被积函数：$f(x) = {sp.latex(expr)}$")
                steps.append(f"2. 不定积分：$\\int f(x) dx = {sp.latex(integral)} + C$")

            # 极限
            limit_0 = sp.limit(expr, x, 0)
            if limit_0 != sp.nan:
                steps.append(f"\n**x→0 极限：**")
                steps.append(f"$\\lim_{{x \\to 0}} {sp.latex(expr)} = {sp.latex(limit_0)}$")

            if not steps:
                steps.append(f"表达式：${sp.latex(expr)}$")
                steps.append(f"简化形式：${sp.latex(sp.simplify(expr))}$")
                steps.append(f"因式分解：${sp.latex(sp.factor(expr))}$")

    except Exception as e:
        # SymPy 无法解析时，生成通用解题框架
        steps = [
            f"**题目：** {problem}",
            "",
            "**解题步骤：**",
            "**步骤 1** — 审题与信息提取：明确题目要求，识别关键已知条件和未知量。",
            "**步骤 2** — 选择方法：根据题目类型确定适用的数学方法和公式。",
            "**步骤 3** — 代入计算：将已知量代入公式，逐步计算。",
            "**步骤 4** — 验证：检查计算过程是否正确，结果是否合理。",
            "**步骤 5** — 作答：给出最终答案和说明。",
        ]

    return "\n".join(steps)


def skill_entry(payload: dict) -> str:
    """生成分步解题过程。"""
    payload = payload or {}
    params = payload.get("params") or {}
    problem = params.get("problem") or payload.get("input", "")
    subject = params.get("subject", "")
    detail_level = params.get("detail_level", "standard")

    if not problem or not problem.strip():
        return "错误：请提供需要分步求解的数学问题。"

    problem = problem.strip()

    header = f"【分步解题】\n"
    if subject:
        header += f"学科：{subject}\n"
    header += f"\n"

    steps = _try_sympy_steps(problem)

    return header + steps
