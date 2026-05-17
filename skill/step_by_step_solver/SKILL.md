---
name: step_by_step_solver
description: 生成数学题目的详细分步解题过程，帮助学生理解每一步的推理逻辑。支持微积分、代数、几何等各类数学题。
---

# step_by_step_solver 技能说明

## 用途
当 Agent 需要展示一道数学题的详细解题步骤时调用本技能：
- 自动将解题过程分解为清晰的步骤
- 每一步附带解释说明
- 支持生成 LaTeX 格式的公式展示
- 适合课后习题讲解、考试题目解析等场景

## 参数
- `problem`：需要分步求解的数学问题
- `subject`：学科领域 (calculus/algebra/geometry/statistics/linear_algebra)
- `detail_level`：详细程度 (brief/standard/detailed)

调用: solver.py
