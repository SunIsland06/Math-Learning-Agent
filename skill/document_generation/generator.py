"""
文档生成技能 —— 将 Markdown 内容转换为 PDF、Word 或 Markdown 文档。

特性：
- PDF 生成：使用 fpdf2，支持中文、页眉页脚、目录
- Word 生成：使用 python-docx，支持标题层级、段落格式
- Markdown 生成：直接保存 Markdown 文本
- 自动保存到用户会话目录，返回下载 URL

入口函数：skill_entry(payload) → str
"""

import re
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, Optional


def skill_entry(payload: dict) -> str:
    """技能入口 —— 根据 Markdown 内容生成文档文件。

    Args:
        payload: {
            "input": str (Markdown 内容),
            "params": {
                "format": "pdf" / "docx" / "md",
                "title": str,
                "author": str,
                "header_text": str,
                "footer_text": str,
                "include_toc": bool,
                "output_dir": str,
                "output_url_prefix": str,
            }
        }

    Returns:
        包含下载链接的 Markdown 文本。
    """
    payload = payload or {}
    params = payload.get("params") or {}
    content = params.get("content") or payload.get("input", "")
    fmt = (params.get("format") or "pdf").lower()
    title = params.get("title", "学习报告")
    author = params.get("author", "")
    header_text = params.get("header_text", "")
    footer_text = params.get("footer_text", "")
    include_toc = params.get("include_toc", True)
    output_dir = params.get("output_dir")
    output_url_prefix = params.get("output_url_prefix", "")

    if not content or not content.strip():
        return "错误：请提供要生成的文档内容（Markdown 格式）。"

    content = content.strip()

    # 确定输出目录
    if output_dir:
        folder = Path(str(output_dir))
    else:
        folder = Path(__file__).resolve().parents[2] / "userdata" / "_generated"
    folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    safe_title = re.sub(r"[^\w一-鿿_-]", "_", title)[:30]

    try:
        if fmt == "docx":
            filepath = _generate_docx(content, title, author, folder, safe_title, timestamp)
        elif fmt == "md":
            filepath = _generate_markdown(content, folder, safe_title, timestamp)
        else:
            filepath = _generate_pdf(content, title, author, header_text, footer_text,
                                     include_toc, folder, safe_title, timestamp)
    except Exception as e:
        return f"【文档生成失败】{fmt} 格式生成时出错: {e}"

    filename = filepath.name
    url = f"{output_url_prefix}{filename}" if output_url_prefix else f"/userdata/_generated/{filename}"

    return (
        f"【文档已生成】\n\n"
        f"标题: {title}\n"
        f"格式: {fmt.upper()}\n"
        f"文件名: {filename}\n\n"
        f"[点击下载文档]({url})\n\n"
        f"下载链接: `{url}`"
    )


# ============================================================
# PDF 生成（使用 fpdf2）
# ============================================================

def _register_cjk_font(pdf) -> str:
    """注册 CJK 中文字体到 fpdf2 实例。

    按优先级尝试多个常见中文字体路径，
    返回注册成功的字体名称，若全部失败则返回 "Helvetica"。

    Args:
        pdf: FPDF 实例

    Returns:
        已注册的字体名称字符串。
    """
    font_candidates = [
        ("微软雅黑常规", r"C:\Windows\Fonts\msyh.ttc"),
        ("微软雅黑粗体", r"C:\Windows\Fonts\msyhbd.ttc"),
        ("宋体", r"C:\Windows\Fonts\simsun.ttc"),
        ("黑体", r"C:\Windows\Fonts\simhei.ttf"),
        ("楷体", r"C:\Windows\Fonts\simkai.ttf"),
        ("微软雅黑", r"C:\Windows\Fonts\msyh.ttf"),
    ]

    for font_label, font_path in font_candidates:
        if not Path(font_path).exists():
            continue
        try:
            pdf.add_font("CJK", "", font_path, uni=True)
            # 尝试也注册粗体（同路径）
            try:
                pdf.add_font("CJK", "B", font_path, uni=True)
            except Exception:
                pass
            return "CJK"
        except Exception:
            continue

    return "Helvetica"

def _generate_pdf(content: str, title: str, author: str,
                  header_text: str, footer_text: str, include_toc: bool,
                  folder: Path, safe_title: str, timestamp: str) -> Path:
    """使用 fpdf2 生成 PDF 文档。

    支持中文（使用内置 Unicode 字体）、页眉页脚和标题格式。

    Args:
        content: Markdown 内容
        title: 文档标题
        author: 作者
        header_text: 页眉文字
        footer_text: 页脚文字
        include_toc: 是否包含目录
        folder: 输出目录
        safe_title: 安全的文件名前缀
        timestamp: 时间戳

    Returns:
        生成的 PDF 文件路径。
    """
    from fpdf import FPDF

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)

    # 注册中文字体
    font_name = _register_cjk_font(pdf)

    # ---- 封面/标题页 ----
    pdf.add_page()
    effective_width = pdf.w - pdf.l_margin - pdf.r_margin
    try:
        pdf.set_font(font_name, "B", 22)
        pdf.ln(40)
        pdf.multi_cell(effective_width, 14, title, align="C")
        pdf.ln(10)

        if author:
            pdf.set_font(font_name, "", 12)
            pdf.cell(effective_width, 10, f"作者: {author}", align="C")
            pdf.ln(10)

        pdf.set_font(font_name, "", 10)
        pdf.cell(effective_width, 10, f"生成时间: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC", align="C")
        pdf.ln(10)
        pdf.cell(effective_width, 10, "由 Math-Learning-Agent 数智教师生成", align="C")
    except Exception:
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(effective_width, 10, f"Title: {title} (PDF generated)", align="C")

    # ---- 目录 ----
    if include_toc:
        toc_items = _extract_toc(content)
        if toc_items:
            pdf.add_page()
            try:
                pdf.set_font(font_name, "B", 16)
                pdf.cell(effective_width, 12, "目录", align="C")
                pdf.ln(14)
                pdf.set_font(font_name, "", 11)
                for level, heading, page_num in toc_items:
                    indent = "    " * (level - 1)
                    prefix = "● " if level == 1 else "  - " if level == 2 else "    · "
                    line = f"{indent}{prefix}{heading}"
                    pdf.cell(effective_width, 8, line)
                    pdf.ln(8)
            except Exception:
                pass

    # ---- 正文 ----
    pdf.add_page()

    # 设置页眉页脚
    if header_text:
        pdf.set_header_font(font_name, "I", 8)
        # fpdf2 header
        pdf.header = lambda: _pdf_header(pdf, font_name, header_text)
    if footer_text:
        pdf.set_footer_font(font_name, "I", 8)
        pdf.footer = lambda: _pdf_footer(pdf, font_name, footer_text)

    # 解析并渲染 Markdown 内容
    _render_markdown_to_pdf(pdf, content, font_name)

    filepath = folder / f"{safe_title}_{timestamp}.pdf"
    pdf.output(str(filepath))
    return filepath


def _pdf_header(pdf, font_name, header_text):
    """PDF 页眉回调。"""
    pdf.set_font(font_name, "I", 8)
    pdf.cell(0, 8, header_text, align="C")
    pdf.ln(10)


def _pdf_footer(pdf, font_name, footer_text):
    """PDF 页脚回调（含页码）。"""
    pdf.set_y(-15)
    pdf.set_font(font_name, "I", 8)
    pdf.cell(0, 10, f"{footer_text}  |  第 {pdf.page_no()} 页", align="C")


def _extract_toc(content: str):
    """从 Markdown 内容中提取目录项。

    Args:
        content: Markdown 文本

    Returns:
        [(level, heading_text, page_estimate), ...]
    """
    toc = []
    for line in content.splitlines():
        match = re.match(r"^(#{1,3})\s+(.+)", line)
        if match:
            level = len(match.group(1))
            heading = match.group(2).strip()
            # 去除 LaTeX 标记用于目录显示
            heading = re.sub(r"\$\$?(.+?)\$\$?", r"\1", heading)
            heading = re.sub(r"[\\[\]{}]", "", heading)
            toc.append((level, heading[:50], 0))
    return toc


def _render_markdown_to_pdf(pdf, content: str, font_name: str):
    """将 Markdown 内容渲染为 PDF 页面。

    Args:
        pdf: FPDF 实例
        content: Markdown 文本
        font_name: 字体名称
    """
    effective_width = pdf.w - pdf.l_margin - pdf.r_margin - 4

    lines = content.splitlines()
    i = 0
    in_code_block = False
    code_buffer = []

    while i < len(lines):
        line = lines[i]

        # 代码块处理
        if line.strip().startswith("```"):
            if in_code_block:
                for cl in code_buffer:
                    try:
                        pdf.set_font("Courier", "", 9)
                        pdf.set_fill_color(240, 240, 240)
                        # 截断过长的行
                        safe_line = cl[:120] if len(cl) > 120 else cl
                        pdf.cell(effective_width, 6, safe_line, fill=True)
                        pdf.ln(6)
                    except Exception:
                        pdf.ln(4)
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # 标题
        h_match = re.match(r"^(#{1,4})\s+(.+)", line)
        if h_match:
            level = len(h_match.group(1))
            heading = h_match.group(2).strip()
            heading = re.sub(r"\$\$?(.+?)\$\$?", r"\1", heading)
            _pdf_section_heading(pdf, font_name, heading, level)
            i += 1
            continue

        # 列表
        if re.match(r"^\s*[-*+]\s+", line):
            try:
                pdf.set_font(font_name, "", 11)
                text = re.sub(r"\$\$?(.+?)\$\$?", r"[公式: \1]", line.strip())
                text = text[2:] if line.strip().startswith("- ") else text[1:]
                pdf.cell(5, 7, "•")
                pdf.multi_cell(effective_width - 5, 7, text)
            except Exception:
                pdf.ln(4)
            i += 1
            continue

        # 水平线
        if re.match(r"^[-*_]{3,}\s*$", line):
            pdf.ln(4)
            pdf.cell(effective_width, 0, "", border="T")
            pdf.ln(4)
            i += 1
            continue

        # 空行
        if not line.strip():
            pdf.ln(4)
            i += 1
            continue

        # 普通段落
        try:
            pdf.set_font(font_name, "", 11)
            text = re.sub(r"\$\$?(.+?)\$\$?", r"[公式: \1]", line.strip())
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
            text = re.sub(r"[*_]{1,3}(.+?)[*_]{1,3}", r"\1", text)
            if text:
                pdf.multi_cell(effective_width, 7, text)
        except Exception:
            pdf.ln(4)
        i += 1


def _pdf_section_heading(pdf, font_name: str, heading: str, level: int):
    """渲染 PDF 章节标题。

    Args:
        pdf: FPDF 实例
        font_name: 字体名称
        heading: 标题文本
        level: 标题层级 (1-4)
    """
    sizes = {1: ("B", 16), 2: ("B", 14), 3: ("B", 12), 4: ("I", 11)}
    style, size = sizes.get(level, ("", 11))
    pdf.ln(4)
    pdf.set_font(font_name, style, size)
    pdf.multi_cell(0, size * 0.6, heading)
    pdf.ln(2)


# ============================================================
# Word 生成（使用 python-docx）
# ============================================================

def _generate_docx(content: str, title: str, author: str,
                   folder: Path, safe_title: str, timestamp: str) -> Path:
    """使用 python-docx 生成 Word 文档。

    Args:
        content: Markdown 内容
        title: 文档标题
        author: 作者
        folder: 输出目录
        safe_title: 安全的文件名前缀
        timestamp: 时间戳

    Returns:
        生成的 .docx 文件路径。
    """
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    doc = Document()

    # 文档属性
    doc.core_properties.title = title
    if author:
        doc.core_properties.author = author

    # ---- 标题页 ----
    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title_para.add_run(title)
    run.font.size = Pt(22)
    run.font.bold = True
    doc.add_paragraph()

    if author:
        author_para = doc.add_paragraph()
        author_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = author_para.add_run(f"作者: {author}")
        run.font.size = Pt(12)

    date_para = doc.add_paragraph()
    date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = date_para.add_run(f"生成时间: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")
    run.font.size = Pt(10)
    doc.add_paragraph()
    doc.add_paragraph()

    # ---- 解析并渲染 Markdown 内容 ----
    _render_markdown_to_docx(doc, content)

    filepath = folder / f"{safe_title}_{timestamp}.docx"
    doc.save(str(filepath))
    return filepath


def _render_markdown_to_docx(doc, content: str):
    """将 Markdown 内容渲染为 Word 文档段落。

    Args:
        doc: python-docx Document 实例
        content: Markdown 文本
    """
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    lines = content.splitlines()
    i = 0
    in_code_block = False
    code_lines = []

    while i < len(lines):
        line = lines[i]

        # 代码块
        if line.strip().startswith("```"):
            if in_code_block:
                for cl in code_lines:
                    code_para = doc.add_paragraph()
                    code_para.style = doc.styles["Normal"]
                    run = code_para.add_run(cl)
                    run.font.name = "Courier New"
                    run.font.size = Pt(9)
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # 标题
        h_match = re.match(r"^(#{1,4})\s+(.+)", line)
        if h_match:
            level = len(h_match.group(1))
            heading_text = h_match.group(2).strip()
            heading_text = re.sub(r"\$\$?(.+?)\$\$?", r"\1", heading_text)
            heading_style = f"Heading {min(level, 4)}"
            para = doc.add_paragraph()
            para.style = doc.styles[heading_style]
            run = para.add_run(heading_text)
            i += 1
            continue

        # 列表
        if re.match(r"^\s*[-*+]\s+", line):
            text = line.strip()[2:] if line.strip().startswith("- ") else line.strip()[1:]
            text = re.sub(r"\$\$?(.+?)\$\$?", r"\1", text)
            para = doc.add_paragraph(text, style="List Bullet")
            i += 1
            continue

        # 水平线
        if re.match(r"^[-*_]{3,}\s*$", line):
            doc.add_paragraph("─" * 60)
            i += 1
            continue

        # 空行
        if not line.strip():
            i += 1
            continue

        # 普通段落
        text = re.sub(r"\$\$?(.+?)\$\$?", r"[公式: \1]", line.strip())
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"[*_]{1,3}(.+?)[*_]{1,3}", r"\1", text)
        if text:
            para = doc.add_paragraph(text)
        i += 1


# ============================================================
# Markdown 生成（直接保存）
# ============================================================

def _generate_markdown(content: str, folder: Path,
                       safe_title: str, timestamp: str) -> Path:
    """直接保存 Markdown 文本文件。

    Args:
        content: Markdown 内容
        folder: 输出目录
        safe_title: 安全的文件名前缀
        timestamp: 时间戳

    Returns:
        生成的 .md 文件路径。
    """
    filepath = folder / f"{safe_title}_{timestamp}.md"
    filepath.write_text(content, encoding="utf-8")
    return filepath
