---
name: wolfram_alpha
description: 查询 Wolfram Alpha 进行复杂数学计算、特殊函数求值、公式推导验证。返回 Wolfram Alpha 的查询结果（文本、图像等）。
---

# wolfram_alpha 技能说明

## 用途
当 Agent 需要进行以下操作时调用本技能：
- 复杂定积分、不定积分的计算和验证
- 特殊函数（Gamma、Beta、Bessel 等）的求值
- 微分方程（ODE/PDE）的解析解
- 极限、级数收敛性判断
- 大数分解、素数判定等数论问题
- 数学常数的精确值查询

## 参数说明
- `query`：要查询的数学表达式或问题（英文或纯数学表达式效果最佳）
- 支持 Wolfram Alpha 的数学语法，如 `integrate x^2 from 0 to 1`、`solve x^3 - 2x + 1 = 0`

调用: wolfram.py
