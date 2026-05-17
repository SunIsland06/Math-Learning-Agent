"""
LaTeX Render Skill —— 使用 matplotlib 渲染 LaTeX 公式为图片。
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
import re
from pathlib import Path
from datetime import datetime


def _render_formula(formula: str, font_size: int = 16, dpi: int = 150) -> bytes:
    """将单个 LaTeX 公式渲染为 PNG 字节。"""
    fig, ax = plt.subplots(figsize=(0.01, 0.01))
    text = ax.text(0.5, 0.5, f"${formula}$", fontsize=font_size,
                   ha="center", va="center", transform=ax.transAxes)

    fig.canvas.draw()
    bbox = text.get_window_extent(renderer=fig.canvas.get_renderer())
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    plt.close(fig)

    # 加入适量边距
    pad = 0.3
    fig, ax = plt.subplots(figsize=(bbox.width + pad * 2, bbox.height + pad * 2))
    ax.text(0.5, 0.5, f"${formula}$", fontsize=font_size,
            ha="center", va="center", transform=ax.transAxes)
    ax.axis("off")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight",
                facecolor="white", edgecolor="none", pad_inches=0.1)
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()


def skill_entry(payload: dict) -> str:
    """渲染 LaTeX 公式为图片。"""
    payload = payload or {}
    params = payload.get("params") or {}
    formula = params.get("formula") or payload.get("input", "")
    font_size = int(params.get("font_size", 16))

    if not formula or not formula.strip():
        return "错误：请提供 LaTeX 公式内容。"

    # 检测是否包含 display math ($$...$$)
    display_pattern = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
    inline_pattern = re.compile(r"\$(.+?)\$")

    display_matches = display_pattern.findall(formula)
    if display_matches:
        formula = display_matches[0].strip()
    else:
        inline_matches = inline_pattern.findall(formula)
        if inline_matches:
            formula = inline_matches[0].strip()

    try:
        img_bytes = _render_formula(formula, font_size=font_size)
    except Exception as e:
        # 回退：用文本渲染
        fig, ax = plt.subplots(figsize=(6, 1))
        ax.text(0.5, 0.5, formula, fontsize=font_size,
                ha="center", va="center", transform=ax.transAxes,
                family="monospace")
        ax.axis("off")
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight",
                    facecolor="white")
        plt.close(fig)
        buf.seek(0)
        img_bytes = buf.getvalue()

    # 持久化到 output_dir（如果有）
    output_dir = params.get("output_dir")
    output_url_prefix = params.get("output_url_prefix", "")
    if output_dir:
        folder = Path(str(output_dir))
        folder.mkdir(parents=True, exist_ok=True)
        filename = f"latex-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.png"
        target = folder / filename
        target.write_bytes(img_bytes)
        url = f"{output_url_prefix}{filename}"
        return (
            f"【LaTeX 公式渲染】\n"
            f"公式: ${formula}$\n"
            f"![{formula}]({url})\n"
            f"图片 URL: {url}"
        )

    b64 = base64.b64encode(img_bytes).decode("ascii")
    return (
        f"【LaTeX 公式渲染】\n"
        f"公式: ${formula}$\n"
        f"![{formula}](data:image/png;base64,{b64})\n"
    )
