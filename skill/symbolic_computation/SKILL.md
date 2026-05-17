---
name: symbolic_computation
description: 基于 SymPy 进行符号计算（求导、积分、极限、方程求解、矩阵运算、级数展开等）。返回精确的解析结果。
---

# symbolic_computation 技能说明

## 用途
当 Agent 需要精确的符号计算结果时调用本技能：
- 求导数（一阶、高阶、偏导数）
- 不定积分和定积分
- 极限计算（包括无穷极限、单侧极限）
- 方程求解（代数方程、微分方程）
- 矩阵运算（行列式、逆矩阵、特征值）
- 级数展开（Taylor/Maclaurin 级数）
- 化简、因式分解、展开
- Laplace/Fourier 变换

## 参数
- `task`：计算类型 (derivative/integral/limit/solve/matrix/series/simplify)
- `expression`：数学表达式（SymPy 语法，如 "x**2 + sin(x)"）
- `variable`：变量名，默认 "x"
- `params`：额外参数，如积分上下限、求导阶数等

调用: symbolic.py
