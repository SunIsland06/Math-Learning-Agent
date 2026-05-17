---
name: latex_render
description: 将 LaTeX 数学公式渲染为高清 PNG 图片，用于需要精美公式展示和复杂数学符号的场景。返回图片 URL 或 base64 数据。
---

# latex_render 技能说明

## 用途
当 Agent 需要展示复杂数学公式、自定义符号、矩阵、分段函数等难以用纯文本表达的数学内容时调用本技能。

## 支持的内容
- 行内公式：$E=mc^2$
- 显示公式：$$\\int_0^\\infty e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}$$
- 矩阵、行列式
- 分段函数
- 自定义符号和字体
- 化学方程式

## 参数
- `formula`：LaTeX 公式内容（可包含多个公式，用 $$ 分隔）
- `font_size`：字体大小，默认 16

调用: renderer.py
