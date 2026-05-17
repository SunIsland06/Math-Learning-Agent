"""
函数图像绘制技能 —— 支持多种图表类型的函数可视化。

支持的图表类型：
- function: 标准函数曲线（默认），支持多函数对比
- parametric: 参数方程（如 x=cos(t), y=sin(t)）
- polar: 极坐标方程（如 r=2*sin(3*theta)）

入口函数：skill_entry(payload) → str
返回：Markdown 格式文本（含 Base64 图片或图片 URL）
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from pathlib import Path
from datetime import datetime


def skill_entry(payload: dict) -> str:
    """技能入口 —— 根据参数绘制函数图像。

    Args:
        payload: {
            "input": str (函数表达式),
            "params": {
                "expressions": [str],       # 表达式列表
                "x_range": [min, max],      # x 轴范围
                "labels": [str],            # 图例标签
                "title": str,               # 图表标题
                "plot_type": str,           # "function" / "parametric" / "polar"
                "output_dir": str,          # 输出目录（可选）
                "output_url_prefix": str,   # URL 前缀（可选）
            }
        }

    Returns:
        包含图像 Markdown 的字符串。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    input_text = payload.get("input", "")

    # 解析表达式列表
    expressions = params.get("expressions", [])
    if not expressions and input_text:
        import re
        expressions = re.findall(r"['\"]([^'\"]+)['\"]", input_text)
        if not expressions:
            expressions = [input_text.strip()]

    if not expressions:
        return "错误：请提供至少一个函数表达式。"

    # 解析 x 轴范围
    x_range = params.get("x_range", [-10, 10])
    if isinstance(x_range, (int, float)):
        x_range = [-x_range, x_range]

    labels = params.get("labels", [])
    title = params.get("title", "")
    plot_type = params.get("plot_type", "function")

    if not labels:
        labels = [f"f{i + 1}(x)" for i in range(len(expressions))]

    fig, ax = plt.subplots(figsize=(8, 5))

    # 按图表类型分发绘图逻辑
    if plot_type == "parametric":
        # 参数方程：t 从 0 到 2π
        t = np.linspace(0, 2 * np.pi, 500)
        for i, expr in enumerate(expressions):
            try:
                x_expr, y_expr = expr.split(",") if "," in expr else (expr, expr)
                x_vals = eval(f"[{x_expr} for t_i in t]", {"t": t, "t_i": t, "np": np, "x": t})
                y_vals = eval(f"[{y_expr} for t_i in t]", {"t": t, "t_i": t, "np": np, "x": t})
                ax.plot(x_vals, y_vals, label=labels[i] if i < len(labels) else f"param {i + 1}")
            except Exception as e:
                ax.text(0.5, 0.5 - i * 0.1, f"参数方程错误: {e}",
                        ha="center", va="center", transform=ax.transAxes, fontsize=10)

    elif plot_type == "polar":
        # 极坐标方程
        theta = np.linspace(0, 2 * np.pi, 500)
        for i, expr in enumerate(expressions):
            try:
                r = eval(expr, {"theta": theta, "t": theta, "np": np, "x": theta})
                ax_polar = fig.add_subplot(111, projection="polar")
                ax_polar.plot(theta, r, label=labels[i] if i < len(labels) else f"r({i + 1})")
                ax = ax_polar
            except Exception as e:
                ax.text(0.5, 0.5 - i * 0.1, f"极坐标错误: {e}",
                        ha="center", va="center", transform=ax.transAxes, fontsize=10)

    else:
        # 标准函数曲线
        x = np.linspace(x_range[0], x_range[1], 500)
        colors = plt.cm.viridis(np.linspace(0, 1, len(expressions)))
        for i, expr in enumerate(expressions):
            try:
                y = eval(expr, {"x": x, "np": np, "math": __import__("math")})
                ax.plot(x, y, label=labels[i] if i < len(labels) else f"f{i + 1}(x)",
                        color=colors[i] if i < len(colors) else None, linewidth=1.5)
            except Exception as e:
                ax.text(0.5, 0.9 - i * 0.08, f"表达式错误 [{expr}]: {e}",
                        ha="center", va="top", transform=ax.transAxes, fontsize=9, color="red")

    # 公共绘图元素
    ax.axhline(y=0, color="gray", linewidth=0.5, linestyle="--")
    ax.axvline(x=0, color="gray", linewidth=0.5, linestyle="--")
    ax.set_title(title or "Function Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    if len(expressions) > 1:
        ax.legend(loc="best")

    # 输出为 PNG
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    img_bytes = buf.getvalue()

    # 持久化到 output_dir（如有）
    output_dir = params.get("output_dir")
    output_url_prefix = params.get("output_url_prefix", "")
    if output_dir:
        folder = Path(str(output_dir))
        folder.mkdir(parents=True, exist_ok=True)
        filename = f"graph-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.png"
        target = folder / filename
        target.write_bytes(img_bytes)
        url = f"{output_url_prefix}{filename}"
        return (
            f"【函数图像】\n"
            f"表达式: {', '.join(expressions)}\n"
            f"![函数图像]({url})\n\n"
            f"图片 URL: {url}"
        )

    # 无 output_dir 时返回 Base64
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return (
        f"【函数图像】\n"
        f"表达式: {', '.join(expressions)}\n"
        f"![函数图像](data:image/png;base64,{b64})\n"
    )
