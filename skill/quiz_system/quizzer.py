"""
测验系统技能 —— 生成阶梯式数学题目、自动批改、推荐相似题目。

核心功能：
1. 出题 (generate): 根据知识点和难度生成阶梯式题目
2. 批改 (grade): 自动比对答案，提供反馈和改进建议
3. 推荐 (recommend): 根据错题推荐相似题目巩固薄弱环节

入口函数：skill_entry(payload) → str
"""

import json
import random
from typing import Any, Dict, List


# ============================================================
# 题库模板 —— 按知识点分类的题目模板
# ============================================================

_QUESTION_TEMPLATES: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "导数": {
        "basic": [
            {"q": "求函数 $f(x) = x^2$ 的导数。", "a": "$f'(x) = 2x$",
             "hint": "使用幂函数求导公式 $\\frac{d}{dx}x^n = nx^{n-1}$"},
            {"q": "求函数 $f(x) = 3x^4$ 的导数。", "a": "$f'(x) = 12x^3$",
             "hint": "常数可提到导数符号外"},
            {"q": "求函数 $f(x) = x^2 + 3x$ 的导数。", "a": "$f'(x) = 2x + 3$",
             "hint": "逐项求导后相加"},
        ],
        "intermediate": [
            {"q": "求函数 $f(x) = x^2 \\sin x$ 的导数。", "a": "$f'(x) = 2x\\sin x + x^2\\cos x$",
             "hint": "使用乘积求导法则 $(uv)' = u'v + uv'$"},
            {"q": "求函数 $f(x) = \\frac{x}{x^2+1}$ 的导数。",
             "a": "$f'(x) = \\frac{1-x^2}{(x^2+1)^2}$",
             "hint": "使用商法则 $(\\frac{u}{v})' = \\frac{u'v - uv'}{v^2}$"},
            {"q": "求函数 $f(x) = e^{2x}$ 的导数。", "a": "$f'(x) = 2e^{2x}$",
             "hint": "使用链式法则，先对外层求导再乘以内层导数"},
        ],
        "advanced": [
            {"q": "求函数 $f(x) = x^x$（$x>0$）的导数。", "a": "$f'(x) = x^x(\\ln x + 1)$",
             "hint": "取对数后隐函数求导：$\\ln y = x\\ln x$"},
            {"q": "求函数 $f(x) = \\ln(\\sin x)$ 的导数。", "a": "$f'(x) = \\cot x$",
             "hint": "链式法则：$\\frac{d}{dx}\\ln u = \\frac{u'}{u}$"},
        ],
    },
    "积分": {
        "basic": [
            {"q": "计算 $\\int x^2 dx$。", "a": "$\\frac{x^3}{3} + C$",
             "hint": "使用幂函数积分公式 $\\int x^n dx = \\frac{x^{n+1}}{n+1} + C$"},
            {"q": "计算 $\\int 2x dx$。", "a": "$x^2 + C$",
             "hint": "先提常数再积分"},
            {"q": "计算 $\\int_0^1 x dx$。", "a": "$\\frac{1}{2}$",
             "hint": "先求不定积分再代入上下限"},
        ],
        "intermediate": [
            {"q": "计算 $\\int x\\cos x dx$。", "a": "$x\\sin x + \\cos x + C$",
             "hint": "使用分部积分法 $\\int u dv = uv - \\int v du$"},
            {"q": "计算 $\\int \\frac{1}{x\\ln x} dx$。", "a": "$\\ln|\\ln x| + C$",
             "hint": "换元法：令 $u = \\ln x$"},
        ],
        "advanced": [
            {"q": "计算 $\\int_0^{\\pi} \\sin^2 x dx$。", "a": "$\\frac{\\pi}{2}$",
             "hint": "使用倍角公式 $\\sin^2 x = \\frac{1-\\cos 2x}{2}$"},
        ],
    },
    "极限": {
        "basic": [
            {"q": "求 $\\lim_{x \\to 0} \\frac{\\sin x}{x}$。", "a": "$1$",
             "hint": "重要极限公式"},
            {"q": "求 $\\lim_{x \\to 0} (1+x)^{\\frac{1}{x}}$。", "a": "$e$",
             "hint": "重要极限公式 $\\lim_{x \\to 0}(1+x)^{\\frac{1}{x}} = e$"},
        ],
        "intermediate": [
            {"q": "求 $\\lim_{x \\to 0} \\frac{e^x - 1}{x}$。", "a": "$1$",
             "hint": "使用洛必达法则或等价无穷小"},
            {"q": "求 $\\lim_{x \\to \\infty} \\frac{\\ln x}{x}$。", "a": "$0$",
             "hint": "使用洛必达法则"},
        ],
        "advanced": [
            {"q": "求 $\\lim_{x \\to 0} \\frac{x - \\sin x}{x^3}$。", "a": "$\\frac{1}{6}$",
             "hint": "使用泰勒展开 $\\sin x = x - \\frac{x^3}{6} + O(x^5)$"},
        ],
    },
    "线性代数": {
        "basic": [
            {"q": "计算矩阵 $\\begin{pmatrix}1&2\\\\3&4\\end{pmatrix}$ 的行列式。", "a": "$-2$",
             "hint": "$\\det\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix} = ad-bc$"},
            {"q": "求向量 $\\vec{a}=(1,2)$ 和 $\\vec{b}=(3,4)$ 的内积。", "a": "$11$",
             "hint": "内积公式：$\\vec{a}\\cdot\\vec{b} = a_1b_1 + a_2b_2$"},
        ],
        "intermediate": [
            {"q": "求矩阵 $\\begin{pmatrix}4&1\\\\2&3\\end{pmatrix}$ 的特征值。", "a": "$\\lambda_1=5, \\lambda_2=2$",
             "hint": "解特征方程 $\\det(A-\\lambda I)=0$"},
        ],
        "advanced": [
            {"q": "判断矩阵 $\\begin{pmatrix}1&2&0\\\\2&5&0\\\\0&0&3\\end{pmatrix}$ 是否正定。", "a": "正定（所有顺序主子式>0）",
             "hint": "检查所有顺序主子式是否大于0"},
        ],
    },
}


def skill_entry(payload: dict) -> str:
    """测验系统入口 —— 出题/批改/推荐。

    Args:
        payload: {
            "input": str,
            "params": {
                "action": "generate" / "grade" / "recommend",
                "topic": str,
                "difficulty": "basic" / "intermediate" / "advanced",
                "count": int,
                "student_answer": str,
                "correct_answer": str,
                "wrong_topics": [str],
            }
        }

    Returns:
        Markdown 格式的测试结果。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    input_text = payload.get("input", "")

    action = params.get("action", "generate")
    topic = params.get("topic", "") or input_text
    difficulty = params.get("difficulty", "basic")
    count = int(params.get("count", 3))

    if action == "grade":
        student_answer = params.get("student_answer", "") or input_text
        correct_answer = params.get("correct_answer", "")
        return _grade_answer(topic, student_answer, correct_answer)

    elif action == "recommend":
        wrong_topics = params.get("wrong_topics", [])
        if not wrong_topics and input_text:
            wrong_topics = [input_text]
        return _recommend_questions(wrong_topics, count)

    else:
        # 默认：出题
        return _generate_quiz(topic, difficulty, count)


def _generate_quiz(topic: str, difficulty: str, count: int) -> str:
    """根据知识点和难度生成测验题。

    Args:
        topic: 知识点名称
        difficulty: 难度等级
        count: 题目数量

    Returns:
        Markdown 格式的题目列表。
    """
    # 查找匹配的题库
    templates = _find_templates(topic, difficulty)
    if not templates:
        return (
            f"【出题提示】\n\n"
            f"当前知识库中暂无「{topic}」的预设题目模板。\n\n"
            f"建议由数智教师根据以下原则自行出题：\n"
            f"1. 基础题（{_diff_label('basic')}）：直接套用公式，考察基本计算能力\n"
            f"2. 进阶题（{_diff_label('intermediate')}）：需要组合多个知识点，考察综合运用\n"
            f"3. 综合题（{_diff_label('advanced')}）：需要分析推理，考察数学思维深度\n\n"
            f"请根据难度「{_diff_label(difficulty)}」生成 {count} 道题目，每道题附带答案和提示。"
        )

    selected = random.sample(templates, min(count, len(templates)))

    lines = [
        f"【阶梯测验 — {topic}】",
        f"难度: {_diff_label(difficulty)}",
        "",
    ]

    for i, item in enumerate(selected, 1):
        lines.append(f"### 题目 {i}")
        lines.append(f"{item['q']}")
        lines.append("")
        lines.append(f"<details>")
        lines.append(f"<summary>查看提示</summary>")
        lines.append(f"{item.get('hint', '请自行推导')}")
        lines.append(f"</details>")
        lines.append("")
        lines.append(f"<details>")
        lines.append(f"<summary>查看答案</summary>")
        lines.append(f"{item['a']}")
        lines.append(f"</details>")
        lines.append("")

    lines.append("---")
    lines.append(f"> 完成答题后，输入你的答案由系统批改。")
    return "\n".join(lines)


def _grade_answer(topic: str, student_answer: str, correct_answer: str) -> str:
    """批改学生答案，提供反馈和改进建议。

    Args:
        topic: 知识点
        student_answer: 学生提交的答案
        correct_answer: 标准答案

    Returns:
        Markdown 格式的批改反馈。
    """
    if not student_answer:
        return "【批改提示】请提供你的答案以便批改。"

    if not correct_answer:
        return (
            f"【批改反馈】\n\n"
            f"你的答案: {student_answer}\n\n"
            f"我无法自动判断答案的对错（缺少标准答案参考）。\n"
            f"请将你的答案和标准答案一并提供，或由数智教师人工判断。"
        )

    # 规范化比对（去除空格、统一格式）
    s_normalized = student_answer.strip().replace(" ", "").replace("\\", "")
    c_normalized = correct_answer.strip().replace(" ", "").replace("\\", "")

    # 简化比对
    if s_normalized == c_normalized:
        return (
            f"【批改结果 — ✅ 正确！】\n\n"
            f"你的答案: {student_answer}\n"
            f"标准答案: {correct_answer}\n\n"
            f"太棒了！答案完全正确。继续加油！\n\n"
            f"> 建议：尝试更难的进阶题目来挑战自己。"
        )
    elif _partial_match(s_normalized, c_normalized):
        return (
            f"【批改结果 — ⚠️ 部分正确】\n\n"
            f"你的答案: {student_answer}\n"
            f"标准答案: {correct_answer}\n\n"
            f"思路大致正确，但答案不够精确。\n"
            f"建议检查计算过程中的符号、系数或简化是否完整。"
        )
    else:
        return (
            f"【批改结果 — ❌ 需要改进】\n\n"
            f"你的答案: {student_answer}\n"
            f"标准答案: {correct_answer}\n\n"
            f"答案与标准结果有较大差异。建议：\n"
            f"1. 回顾相关知识点和公式\n"
            f"2. 检查推导过程中的每一步\n"
            f"3. 如有疑问，请向数智教师提问获取详细讲解\n\n"
            f"> 提示：可以要求系统推荐相似题目来巩固这个知识点。"
        )


def _recommend_questions(wrong_topics: List[str], count: int) -> str:
    """根据错题知识点推荐相似题目。

    Args:
        wrong_topics: 做错的知识点列表
        count: 推荐题目数量

    Returns:
        Markdown 格式的推荐题目列表。
    """
    lines = [
        "【相似题目推荐 — 巩固薄弱环节】",
        "",
    ]

    all_questions = []
    for topic in wrong_topics:
        # 找相关知识点的基础和进阶题
        for diff in ["basic", "intermediate"]:
            templates = _find_templates(topic, diff)
            for t in templates:
                if t not in all_questions:
                    all_questions.append((topic, diff, t))

    if not all_questions:
        for topic in wrong_topics:
            lines.append(f"### {topic}")
            lines.append("")
            lines.append(f"当前题库中暂无「{topic}」的预设题目。")
            lines.append("建议由数智教师根据该知识点自行设计 2-3 道练习题。")
            lines.append("")
        return "\n".join(lines)

    selected = random.sample(all_questions, min(count, len(all_questions)))

    for i, (topic, diff, item) in enumerate(selected, 1):
        lines.append(f"### 推荐题 {i} — {topic}（{_diff_label(diff)}）")
        lines.append(f"{item['q']}")
        if item.get('hint'):
            lines.append(f"_提示: {item['hint']}_")
        lines.append("")

    lines.append("---")
    lines.append("> 完成这些题目后，系统可以再次批改并提供反馈。薄弱环节需要反复练习才能巩固。")
    return "\n".join(lines)


def _find_templates(topic: str, difficulty: str) -> List[Dict[str, Any]]:
    """查找匹配的题目模板。

    先在精确匹配的知识点中找对应难度，
    若无则跨难度搜索，
    再回退到模糊匹配。

    Args:
        topic: 知识点名称
        difficulty: 难度等级

    Returns:
        匹配的题目模板列表。
    """
    # 精确匹配
    if topic in _QUESTION_TEMPLATES:
        templates = _QUESTION_TEMPLATES[topic]
        if difficulty in templates:
            return templates[difficulty]
        # 跨难度
        all_qs = []
        for diff_qs in templates.values():
            all_qs.extend(diff_qs)
        return all_qs

    # 模糊匹配（关键词包含）
    for key in _QUESTION_TEMPLATES:
        if key in topic or topic in key:
            templates = _QUESTION_TEMPLATES[key]
            all_qs = []
            for diff_qs in templates.values():
                all_qs.extend(diff_qs)
            return all_qs

    return []


def _partial_match(s1: str, s2: str) -> bool:
    """检查两个规范化字符串是否部分匹配。

    忽略大小写差异和常见等价变形。

    Args:
        s1: 学生答案（规范化后）
        s2: 标准答案（规范化后）

    Returns:
        是否部分匹配。
    """
    if len(s1) < 3 or len(s2) < 3:
        return False
    # 检查是否共享关键数值或表达式
    common_chars = set(s1) & set(s2)
    if len(common_chars) >= min(len(s1), len(s2)) * 0.5:
        return True
    return False


def _diff_label(difficulty: str) -> str:
    """难度标签映射。"""
    return {
        "basic": "基础 ⭐",
        "intermediate": "进阶 ⭐⭐",
        "advanced": "综合 ⭐⭐⭐",
    }.get(difficulty, difficulty)
