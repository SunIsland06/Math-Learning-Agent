---
name: graph_plotting
description: 绘制2D函数图像，支持单函数、多函数对比、参数方程、极坐标、隐函数等。返回 PNG 图像 URL 或 base64 数据。
---

# graph_plotting 技能说明

## 用途
当 Agent 需要绘制函数图像来辅助数学教学时调用本技能：
- 单函数曲线：y=f(x)
- 多函数对比：同时绘制多条曲线
- 参数方程：x=f(t), y=g(t)
- 极坐标：r=f(theta)
- 散点图、数据可视化
- 标注特殊点（极值、零点、交点等）

## 参数
- `expressions`：函数表达式列表，如 ["x**2", "2*x+1"]
- `x_range`：x轴范围，如 [-5, 5]
- `labels`：图例标签列表
- `title`：图表标题
- `plot_type`：图表类型 (function/parametric/polar/scatter)

调用: plotter.py
