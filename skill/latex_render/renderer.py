"""
LaTeX 公式渲染技能 —— 使用 matplotlib 将 LaTeX 公式渲染为高清 PNG 图片。

特性：
- 支持 inline ($...$) 和 display ($$...$$) 两种公式格式
- 自动计算公式边界框，裁剪到最小尺寸
- 支持自定义字体大小和 DPI
- 持久化到 output_dir 或返回 Base64 Data URI

入口函数：skill_entry(payload) → str
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
    """将单个 LaTeX 公式渲染为 PNG 字节数据。

    使用两遍渲染策略：
    1. 先渲染到临时画布，计算文本的实际边界框
    2. 再按精确尺寸创建最终画布，确保无多余留白

    Args:
        formula: LaTeX 公式内容（不含 $ 定界符）
        font_size: 字体大小
        dpi: 输出分辨率

    Returns:
        PNG 图片字节数据。
    """
    # 第一遍：测量文本边界框
    fig, ax = plt.subplots(figsize=(0.01, 0.01))
    text = ax.text(0.5, 0.5, f"${formula}$", fontsize=font_size,
                   ha="center", va="center", transform=ax.transAxes)

    fig.canvas.draw()
    bbox = text.get_window_extent(renderer=fig.canvas.get_renderer())
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    plt.close(fig)

    # 第二遍：按精确尺寸渲染
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
    """技能入口 —— 渲染 LaTeX 公式为图片。

    Args:
        payload: {
            "input": str (LaTeX 公式，可含 $ 定界符),
            "params": {
                "formula": str,           # LaTeX 公式
                "font_size": int,         # 字体大小（默认 16）
                "output_dir": str,        # 输出目录（可选）
                "output_url_prefix": str, # URL 前缀（可选）
            }
        }

    Returns:
        包含渲染结果（图片 URL 或 Base64）的 Markdown 文本。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    formula = params.get("formula") or payload.get("input", "")
    font_size = int(params.get("font_size", 16))

    if not formula or not formula.strip():
        return "错误：请提供 LaTeX 公式内容。"

    # 提取纯公式内容（去除 $ 定界符）
    display_pattern = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
    inline_pattern = re.compile(r"\$(.+?)\$")

    display_matches = display_pattern.findall(formula)
    if display_matches:
        formula = display_matches[0].strip()
    else:
        inline_matches = inline_pattern.findall(formula)
        if inline_matches:
            formula = inline_matches[0].strip()

    # 渲染公式
    try:
        img_bytes = _render_formula(formula, font_size=font_size)
    except Exception:
        # LaTeX 渲染失败时回退为纯文本渲染
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

    # 持久化到 output_dir（如有）
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

    # 回退为 Base64 Data URI
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return (
        f"【LaTeX 公式渲染】\n"
        f"公式: ${formula}$\n"
        f"![{formula}](data:image/png;base64,{b64})\n"
    )
