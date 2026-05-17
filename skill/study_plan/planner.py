"""
学习计划生成技能 —— 根据用户目标、知识薄弱点和教材内容生成个性化学习计划。

计划类型：
- study: 新知识学习计划（按章节递进）
- review: 复习计划（重点回顾薄弱环节）
- exam: 备考计划（全面复习 + 模拟练习 + 查漏补缺）

计划结构：
1. 总体概览（目标、时间、覆盖范围）
2. 每日学习安排（知识点 + 练习题 + 预计时间）
3. 阶段性测试节点
4. 错题复习提示

入口函数：skill_entry(payload) → str
"""

import json
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List


def skill_entry(payload: dict) -> str:
    """生成个性化学习计划。

    Args:
        payload: {
            "input": str (用户的学习目标描述),
            "params": {
                "subject": str,
                "duration_days": int,
                "daily_minutes": int,
                "weak_points": [str],
                "topics": [str],
                "plan_type": "study" / "review" / "exam",
            }
        }

    Returns:
        Markdown 格式的结构化学习计划。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    goal = params.get("goal") or payload.get("input", "")

    subject = params.get("subject", "高等数学")
    duration_days = int(params.get("duration_days", 7))
    daily_minutes = int(params.get("daily_minutes", 60))
    weak_points = params.get("weak_points", [])
    topics = params.get("topics", [])
    plan_type = params.get("plan_type", "study")

    if not goal and not topics:
        return "错误：请提供学习目标或需要覆盖的知识点列表。"

    # 确保参数合理
    duration_days = max(1, min(duration_days, 90))
    daily_minutes = max(30, min(daily_minutes, 480))

    # 根据计划类型生成不同的结构
    if plan_type == "review":
        return _generate_review_plan(goal, subject, duration_days, daily_minutes, weak_points, topics)
    elif plan_type == "exam":
        return _generate_exam_plan(goal, subject, duration_days, daily_minutes, weak_points, topics)
    else:
        return _generate_study_plan(goal, subject, duration_days, daily_minutes, topics)


def _generate_study_plan(goal: str, subject: str, days: int, minutes: int,
                          topics: List[str]) -> str:
    """生成新知识学习计划。"""
    today = datetime.now(timezone.utc)
    plan_lines = [
        f"# {subject} 学习计划",
        "",
        f"**学习目标**: {goal}",
        f"**计划周期**: {days} 天（{today.strftime('%Y-%m-%d')} — {(today + timedelta(days=days - 1)).strftime('%Y-%m-%d')}）",
        f"**每日学习时长**: {minutes} 分钟",
        f"**计划类型**: 新知识学习",
        "",
        "---",
        "",
        "## 学习策略",
        "",
        "1. **预习**（10%时间）：快速浏览当天知识点，建立整体框架",
        "2. **精学**（50%时间）：深入学习核心概念，理解定理推导过程",
        "3. **练习**（30%时间）：完成配套习题，从基础到进阶",
        "4. **总结**（10%时间）：整理笔记，标注重点和疑惑",
        "",
        "---",
        "",
        "## 每日学习安排",
        "",
    ]

    if topics:
        topics_per_day = max(1, len(topics) // days)
        for day in range(1, days + 1):
            date = today + timedelta(days=day - 1)
            day_topics = topics[(day - 1) * topics_per_day: day * topics_per_day]
            if not day_topics and topics:
                day_topics = [topics[-1]]

            plan_lines.append(f"### 第 {day} 天 — {date.strftime('%m/%d')}（{_day_name(date)}）")
            plan_lines.append("")
            plan_lines.append(f"**学习内容**:")
            for t in day_topics:
                plan_lines.append(f"- {t}")
            if not day_topics:
                plan_lines.append(f"- 综合复习与练习")

            plan_lines.append("")
            plan_lines.append(f"**时间分配**（共 {minutes} 分钟）:")
            plan_lines.append(f"- 预习: {minutes * 10 // 100} 分钟")
            plan_lines.append(f"- 精学: {minutes * 50 // 100} 分钟")
            plan_lines.append(f"- 练习: {minutes * 30 // 100} 分钟")
            plan_lines.append(f"- 总结: {minutes * 10 // 100} 分钟")

            plan_lines.append("")
            plan_lines.append("**练习题**:")
            plan_lines.append("- [ ] 基础概念辨析题（3-5道）")
            plan_lines.append("- [ ] 计算推导题（2-3道）")
            plan_lines.append("- [ ] 综合应用题（1-2道）")
            plan_lines.append("")
    else:
        for day in range(1, days + 1):
            date = today + timedelta(days=day - 1)
            plan_lines.append(f"### 第 {day} 天 — {date.strftime('%m/%d')}（{_day_name(date)}）")
            plan_lines.append("")
            plan_lines.append(f"**时间分配**（共 {minutes} 分钟）: 预习 {minutes*10//100}min | 精学 {minutes*50//100}min | 练习 {minutes*30//100}min | 总结 {minutes*10//100}min")
            plan_lines.append("")

    # 阶段测试
    mid_day = days // 2
    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 阶段性检测")
    plan_lines.append("")
    plan_lines.append(f"- **第 {max(1, mid_day)} 天**: 中期测试 —— 覆盖前半段知识点，检测学习效果")
    plan_lines.append(f"- **第 {days} 天**: 期末测试 —— 全面检测，综合评估学习成果")
    plan_lines.append("")
    plan_lines.append("## 建议")
    plan_lines.append("")
    plan_lines.append("- 每日学习结束后在对话中记录掌握情况，系统会自动更新学习画像")
    plan_lines.append("- 遇到困难的知识点可以随时向数智教师提问")
    plan_lines.append("- 建议将练习题答案拍照或输入，由系统批改并提供反馈")
    plan_lines.append("- 每周回顾错题本，针对薄弱环节追加练习")
    plan_lines.append("")

    return "\n".join(plan_lines)


def _generate_review_plan(goal: str, subject: str, days: int, minutes: int,
                           weak_points: List[str], topics: List[str]) -> str:
    """生成复习计划（重点攻克薄弱环节）。"""
    today = datetime.now(timezone.utc)
    plan_lines = [
        f"# {subject} 复习计划",
        "",
        f"**复习目标**: {goal}",
        f"**计划周期**: {days} 天（{today.strftime('%Y-%m-%d')} — {(today + timedelta(days=days - 1)).strftime('%Y-%m-%d')}）",
        f"**每日学习时长**: {minutes} 分钟",
        f"**计划类型**: 针对性复习",
        "",
    ]

    if weak_points:
        plan_lines.append("## 重点攻克：薄弱知识点")
        plan_lines.append("")
        for i, wp in enumerate(weak_points, 1):
            plan_lines.append(f"{i}. **{wp}** —— 需要重点回顾和加强练习")
        plan_lines.append("")

    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 复习方法论")
    plan_lines.append("")
    plan_lines.append("1. **错题重温**（20%）：先回顾之前做错的题目，理解错误原因")
    plan_lines.append("2. **知识巩固**（40%）：重新学习薄弱知识点的教材内容和推导过程")
    plan_lines.append("3. **强化练习**（30%）：针对薄弱环节集中做题，从基础到变式")
    plan_lines.append("4. **归纳总结**（10%）：制作思维导图，梳理知识体系")
    plan_lines.append("")
    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 每日复习安排")
    plan_lines.append("")

    all_items = weak_points + topics
    if not all_items:
        all_items = [f"{subject}核心知识点"]

    items_per_day = max(1, len(all_items) // days)
    for day in range(1, days + 1):
        date = today + timedelta(days=day - 1)
        day_items = all_items[(day - 1) * items_per_day: day * items_per_day]
        if not day_items and all_items:
            day_items = [all_items[-1]]

        plan_lines.append(f"### 第 {day} 天 — {date.strftime('%m/%d')}（{_day_name(date)}）")
        plan_lines.append("")
        for item in day_items:
            plan_lines.append(f"- **复习**: {item}")
        plan_lines.append(f"- **练习题**: 3-5道针对性题目")
        plan_lines.append(f"- **预计时长**: {minutes} 分钟")
        plan_lines.append("")

    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 复习检测表")
    plan_lines.append("")
    for i, item in enumerate(all_items[:10], 1):
        plan_lines.append(f"- [ ] {item}")
    plan_lines.append("")
    plan_lines.append("> 每天复习后勾选对应项目，目标是在计划结束前全部掌握。")
    plan_lines.append("")

    return "\n".join(plan_lines)


def _generate_exam_plan(goal: str, subject: str, days: int, minutes: int,
                         weak_points: List[str], topics: List[str]) -> str:
    """生成备考冲刺计划。"""
    today = datetime.now(timezone.utc)
    plan_lines = [
        f"# {subject} 备考计划",
        "",
        f"**备考目标**: {goal}",
        f"**备考周期**: {days} 天（{today.strftime('%Y-%m-%d')} — {(today + timedelta(days=days - 1)).strftime('%Y-%m-%d')}）",
        f"**每日学习时长**: {minutes} 分钟",
        f"**计划类型**: 备考冲刺",
        "",
        "---",
        "",
        "## 备考三阶段",
        "",
    ]

    phase1_days = max(1, days // 3)
    phase2_days = max(1, days // 3)
    phase3_days = days - phase1_days - phase2_days

    plan_lines.append(f"### 第一阶段：系统梳理（第 1-{phase1_days} 天）")
    plan_lines.append("")
    plan_lines.append(f"- 全面梳理{subject}知识体系，建立知识框架")
    plan_lines.append("- 逐章节复习教材内容，确保基础概念清晰")
    plan_lines.append("- 完成课后基础习题，巩固基本方法")
    plan_lines.append("- 制作公式和定理速查表")
    plan_lines.append("")

    plan_lines.append(f"### 第二阶段：强化训练（第 {phase1_days + 1}-{phase1_days + phase2_days} 天）")
    plan_lines.append("")
    plan_lines.append("- 集中攻克重点难点和易错题型")
    plan_lines.append("- 完成近3年真题或模拟题")
    plan_lines.append("- 限时训练，提升解题速度和准确率")
    if weak_points:
        plan_lines.append("- 针对以下薄弱环节进行专题训练：")
        for wp in weak_points[:5]:
            plan_lines.append(f"  - {wp}")
    plan_lines.append("")

    plan_lines.append(f"### 第三阶段：冲刺模拟（第 {phase1_days + phase2_days + 1}-{days} 天）")
    plan_lines.append("")
    plan_lines.append("- 全真模拟考试（限时、闭卷）")
    plan_lines.append("- 查漏补缺，回顾错题和标记题")
    plan_lines.append("- 调整心态，复习公式速查表")
    plan_lines.append("- 重点是保证已掌握的知识不丢分")
    plan_lines.append("")

    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 每日时间表示例")
    plan_lines.append("")
    plan_lines.append(f"| 时间段 | 内容 | 时长 |")
    plan_lines.append(f"|--------|------|------|")
    plan_lines.append(f"| 前 {minutes * 10 // 100} 分钟 | 知识回顾 + 错题重温 | {minutes * 10 // 100} min |")
    plan_lines.append(f"| 中间 {minutes * 60 // 100} 分钟 | 核心学习/做题训练 | {minutes * 60 // 100} min |")
    plan_lines.append(f"| 最后 {minutes * 30 // 100} 分钟 | 总结归纳 + 错题整理 | {minutes * 30 // 100} min |")
    plan_lines.append("")

    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 备考资源清单")
    plan_lines.append("")
    plan_lines.append("- [ ] 教材知识点梳理完成")
    plan_lines.append("- [ ] 公式速查表制作完成")
    plan_lines.append("- [ ] 近3年真题练习完成")
    plan_lines.append("- [ ] 模拟考试完成（至少2次）")
    plan_lines.append("- [ ] 错题本回顾完成")
    plan_lines.append("")
    plan_lines.append("> 每完成一项请勾选，保持备考节奏。加油！")
    plan_lines.append("")

    return "\n".join(plan_lines)


def _day_name(date) -> str:
    """获取中文星期名。"""
    names = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    return names[date.weekday()]
