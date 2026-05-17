---
name: study_plan
description: 根据用户的知识薄弱点、记忆数据和教材知识库，生成个性化的学习计划或复习计划，包含每日学习内容、练习题、复习时间安排等。
---

## 使用说明
当用户请求生成学习计划、复习计划、备考计划时调用此技能。

## 参数
- **input**: 用户的学习目标或计划需求描述
- **params**:
  - `subject`: 学科名称（高等数学 / 线性代数 / 离散数学，可选）
  - `duration_days`: 计划总天数（默认 7）
  - `daily_minutes`: 每日学习时长（分钟，默认 60）
  - `weak_points`: 薄弱知识点列表（可选，从长期记忆中提取）
  - `topics`: 需要覆盖的知识点列表（可选，从知识库中提取）
  - `plan_type`: 计划类型 —— "study"（学习计划）/ "review"（复习计划）/ "exam"（备考计划）
  - `output_dir`: 输出目录路径
  - `output_url_prefix`: URL 前缀

调用: planner.py
