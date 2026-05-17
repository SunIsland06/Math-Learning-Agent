---
name: quiz_system
description: 生成阶梯式数学测验题、自动批改学生答案、推荐相似题目巩固薄弱点。支持生成试卷和练习集。
---

## 使用说明
当需要生成练习题、测验题、批改答案或推荐相似题目时调用此技能。

## 功能
1. **出题**: 根据知识点和难度生成阶梯式题目（基础→进阶→综合）
2. **批改**: 自动比对答案，给出对错判断和改进建议
3. **推荐**: 根据错题自动推荐相似题目巩固薄弱环节

## 参数
- **input**: 题目描述或学生答案
- **params**:
  - `action`: 操作类型 —— "generate"（出题）/ "grade"（批改）/ "recommend"（推荐相似题）
  - `topic`: 知识点名称
  - `difficulty`: 难度等级 —— "basic" / "intermediate" / "advanced"
  - `count`: 题目数量（默认 3）
  - `student_answer`: 学生答案（批改模式）
  - `correct_answer`: 正确答案（批改模式）
  - `wrong_topics`: 做错的知识点列表（推荐模式）

调用: quizzer.py
