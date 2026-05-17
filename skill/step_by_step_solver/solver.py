"""
分步解题技能 —— 为数学题目生成逐步推理过程。

支持两种模式：
1. SymPy 自动解析 —— 识别表达式并生成导数/积分/极限/方程求解步骤
2. 通用解题框架 —— SymPy 无法解析时提供标准解题模板

预处理规则：
- 将 ^ 替换为 **（幂运算）
- 补全隐式乘法（如 5x → 5*x, 2(x+1) → 2*(x+1)）
- 去掉前置命令词（solve/calculate/find/...）

入口函数：skill_entry(payload) → str
"""

import re
import sympy as sp


def _preprocess_math(problem: str) -> str:
    """预处理数学表达式，将常见数学语法转为 SymPy 可解析格式。

    处理规则：
    1. 去掉前置英文命令词（solve/calculate/find/...）
    2. ^ → ** （幂运算）
    3. 数字后接字母 → 补乘号（5x → 5*x）
    4. )数字 → )*数字
    5. 数字( → 数字*(

    Args:
        problem: 原始问题文本

    Returns:
        预处理后的表达式字符串。
    """
    text = problem.strip()
    # 去掉前置命令词
    text = re.sub(
        r"^(solve|calculate|find|compute|evaluate|determine|verify|simplify|expand|factor|differentiate|integrate)\s+",
        "", text, flags=re.IGNORECASE,
    )
    # ^ → **
    text = re.sub(r"(\w+|\))\s*\^\s*(\w+|\(|-)", r"\1**\2", text)
    # 隐式乘法：数字后接字母
    text = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", text)
    # )数字 → )*数字
    text = re.sub(r"\)(\d)", r")*\1", text)
    # 数字( → 数字*(
    text = re.sub(r"(\d)\(", r"\1*(", text)
    return text


def _try_sympy_steps(problem: str) -> str:
    """尝试用 SymPy 自动解析问题并生成解题步骤。

    支持：
    - 方程（含 = 号）→ 求解
    - 表达式 → 导数 + 积分 + 极限分析
    - 回退 → 表达式化简/因式分解

    Args:
        problem: 预处理后的数学问题

    Returns:
        Markdown 格式的分步解题文本。
    """
    x = sp.Symbol("x")
    processed = _preprocess_math(problem)
    steps = []

    try:
        if "=" in processed:
            # ---- 方程求解 ----
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
            # ---- 表达式分析 ----
            expr = sp.sympify(processed)

            # 求导
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

            # 极限（x→0）
            limit_0 = sp.limit(expr, x, 0)
            if limit_0 != sp.nan:
                steps.append(f"\n**x→0 极限：**")
                steps.append(f"$\\lim_{{x \\to 0}} {sp.latex(expr)} = {sp.latex(limit_0)}$")

            # 无特殊操作时的回退
            if not steps:
                steps.append(f"表达式：${sp.latex(expr)}$")
                steps.append(f"简化形式：${sp.latex(sp.simplify(expr))}$")
                steps.append(f"因式分解：${sp.latex(sp.factor(expr))}$")

    except Exception:
        # SymPy 无法解析时提供通用解题框架
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
    """技能入口 —— 生成数学题目的分步解题过程。

    Args:
        payload: {
            "input": str (问题文本),
            "params": {
                "problem": str,         # 数学问题
                "subject": str,         # 学科分类（可选）
                "detail_level": str,    # 详细程度（"brief"/"standard"/"detailed"）
            }
        }

    Returns:
        Markdown 格式的分步解题文本。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    problem = params.get("problem") or payload.get("input", "")
    subject = params.get("subject", "")
    detail_level = params.get("detail_level", "standard")

    if not problem or not problem.strip():
        return "错误：请提供需要分步求解的数学问题。"

    problem = problem.strip()

    header = "【分步解题】\n"
    if subject:
        header += f"学科：{subject}\n"
    header += "\n"

    steps = _try_sympy_steps(problem)

    return header + steps
