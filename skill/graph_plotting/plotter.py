"""
Graph Plotting Skill —— 绘制函数图像，支持多种图表类型。
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
    """绘制函数图像。"""
    payload = payload or {}
    params = payload.get("params") or {}
    input_text = payload.get("input", "")

    # 解析参数
    expressions = params.get("expressions", [])
    if not expressions and input_text:
        # 尝试从 input 中解析表达式
        import re
        expressions = re.findall(r"['\"]([^'\"]+)['\"]", input_text)
        if not expressions:
            expressions = [input_text.strip()]

    if not expressions:
        return "错误：请提供至少一个函数表达式。"

    x_range = params.get("x_range", [-10, 10])
    if isinstance(x_range, (int, float)):
        x_range = [-x_range, x_range]
    labels = params.get("labels", [])
    title = params.get("title", "")
    plot_type = params.get("plot_type", "function")

    if not labels:
        labels = [f"f{i+1}(x)" for i in range(len(expressions))]

    fig, ax = plt.subplots(figsize=(8, 5))

    if plot_type == "parametric":
        t = np.linspace(0, 2 * np.pi, 500)
        for i, expr in enumerate(expressions):
            try:
                x_expr, y_expr = expr.split(",") if "," in expr else (expr, expr)
                x_vals = eval(f"[{x_expr} for t_i in t]", {"t": t, "t_i": t, "np": np, "x": t})
                y_vals = eval(f"[{y_expr} for t_i in t]", {"t": t, "t_i": t, "np": np, "x": t})
                ax.plot(x_vals, y_vals, label=labels[i] if i < len(labels) else f"param {i+1}")
            except Exception as e:
                ax.text(0.5, 0.5 - i * 0.1, f"参数方程错误: {e}",
                        ha="center", va="center", transform=ax.transAxes, fontsize=10)
    elif plot_type == "polar":
        theta = np.linspace(0, 2 * np.pi, 500)
        for i, expr in enumerate(expressions):
            try:
                r = eval(expr, {"theta": theta, "t": theta, "np": np, "x": theta})
                ax_polar = fig.add_subplot(111, projection='polar')
                ax_polar.plot(theta, r, label=labels[i] if i < len(labels) else f"r({i+1})")
                ax = ax_polar
            except Exception as e:
                ax.text(0.5, 0.5 - i * 0.1, f"极坐标错误: {e}",
                        ha="center", va="center", transform=ax.transAxes, fontsize=10)
    else:
        x = np.linspace(x_range[0], x_range[1], 500)
        colors = plt.cm.viridis(np.linspace(0, 1, len(expressions)))
        for i, expr in enumerate(expressions):
            try:
                y = eval(expr, {"x": x, "np": np, "math": __import__("math")})
                ax.plot(x, y, label=labels[i] if i < len(labels) else f"f{i+1}(x)",
                        color=colors[i] if i < len(colors) else None, linewidth=1.5)
            except Exception as e:
                ax.text(0.5, 0.9 - i * 0.08, f"表达式错误 [{expr}]: {e}",
                        ha="center", va="top", transform=ax.transAxes, fontsize=9, color="red")

    ax.axhline(y=0, color="gray", linewidth=0.5, linestyle="--")
    ax.axvline(x=0, color="gray", linewidth=0.5, linestyle="--")
    ax.set_title(title or "Function Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    if len(expressions) > 1:
        ax.legend(loc="best")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    img_bytes = buf.getvalue()

    # 持久化
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

    b64 = base64.b64encode(img_bytes).decode("ascii")
    return (
        f"【函数图像】\n"
        f"表达式: {', '.join(expressions)}\n"
        f"![函数图像](data:image/png;base64,{b64})\n"
    )
