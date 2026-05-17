"""
教材 Markdown 分块模块 —— 将教科书 .md 文件按标题层级切分为适合向量化的文本块。

分块策略：
1. 按 Markdown 标题（# ~ ######）将文档切分为章节段落
2. 在每个章节内按空行分段，以段落为最小单位累积到 ~1000 字符
3. 相邻块之间有 120 字符的重叠区域，防止语义断裂
4. 过小的块（<200 字符）自动合并到相邻块

输出文件：
- chunks_result.json: 结构化分块数据
- chunks_preview.txt: 人类可读的分块预览
"""

import os
import sys
import json
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from utils.encoding_setup import setup_windows_utf8
setup_windows_utf8()

HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)$")
IMAGE_RE = re.compile(r"^!\[.*?\]\(.*?\)\s*$")

DEFAULT_MAX_CHARS = 1000
DEFAULT_OVERLAP_CHARS = 120
DEFAULT_MIN_CHARS = 200


def _clean_lines(lines):
    """清洗行列表：去除纯图片行和 HTML 表格标签。"""
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            cleaned.append("")
            continue
        if IMAGE_RE.match(stripped):
            continue
        if stripped.startswith("<table") or stripped.startswith("</table"):
            continue
        cleaned.append(line)
    return cleaned


def _iter_sections(lines):
    """按 Markdown 标题迭代产生章节。

    每个章节包含：
    - header_path: 当前标题层级路径（如 ["第一章", "1.1 导数概念"]）
    - start_line: 起始行号
    - lines: 章节内的所有行

    Yields:
        dict: {"header_path": [...], "start_line": int, "lines": [...]}
    """
    headers = []
    current = []
    start_line = 1

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        match = HEADER_RE.match(stripped)
        if match:
            if current:
                yield {
                    "header_path": headers[:],
                    "start_line": start_line,
                    "lines": current,
                }
                current = []
            level = len(match.group(1))
            title = match.group(2).strip() or "未命名章节"
            # 同级或上级标题出现时回退层级
            if len(headers) >= level:
                headers = headers[: level - 1]
            headers.append(title)
            start_line = idx
        current.append(line)

    if current:
        yield {
            "header_path": headers[:],
            "start_line": start_line,
            "lines": current,
        }


def _split_paragraphs(paragraphs, max_chars, overlap_chars):
    """在 max_chars 约束下按段落边界切分文本块。

    优先在段落边界处分割，避免切断完整段落。
    若单个段落超过 max_chars，则硬切分。

    Args:
        paragraphs: 段落文本列表
        max_chars: 每块最大字符数
        overlap_chars: 块间重叠字符数

    Returns:
        文本块字符串列表。
    """
    chunks = []
    current = []
    current_len = 0

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        paragraph_len = len(paragraph)

        extra_len = paragraph_len + (2 if current else 0)
        if current_len + extra_len <= max_chars:
            current.append(paragraph)
            current_len += extra_len
            continue

        # 当前累积块达到上限，保存并开始新块（带重叠）
        if current:
            chunk = "\n\n".join(current).strip()
            chunks.append(chunk)
            overlap_text = chunk[-overlap_chars:] if overlap_chars > 0 else ""
            current = [overlap_text, paragraph] if overlap_text else [paragraph]
            current_len = len("\n\n".join(current))
        else:
            # 单段过长时硬切分
            start = 0
            while start < paragraph_len:
                end = min(start + max_chars, paragraph_len)
                chunks.append(paragraph[start:end].strip())
                start = end
            current = []
            current_len = 0

    if current:
        chunks.append("\n\n".join(current).strip())

    return chunks


def _merge_small_chunks(chunks, min_chars, max_chars):
    """合并过小的文本块到相邻块中。

    Args:
        chunks: 文本块列表
        min_chars: 最小块大小阈值
        max_chars: 合并后最大块大小

    Returns:
        合并后的文本块列表。
    """
    merged = []
    buffer = ""
    for chunk in chunks:
        if not buffer:
            buffer = chunk
            continue
        if len(buffer) < min_chars and len(buffer) + 2 + len(chunk) <= max_chars:
            buffer = buffer + "\n\n" + chunk
            continue
        merged.append(buffer)
        buffer = chunk
    if buffer:
        merged.append(buffer)
    return merged


def split_markdown_by_headers(content: str, max_chunk_len=DEFAULT_MAX_CHARS,
                               overlap_chars=DEFAULT_OVERLAP_CHARS,
                               min_chunk_len=DEFAULT_MIN_CHARS):
    """将 Markdown 全文按标题层级分段并切块。

    这是分块的主入口函数。

    Args:
        content: Markdown 文件全文
        max_chunk_len: 每块最大字符数（默认 1000）
        overlap_chars: 块间重叠字符数（默认 120）
        min_chunk_len: 最小块大小（默认 200）

    Returns:
        [{"heading_path": str, "start_line": int, "content": str}, ...]
    """
    lines = _clean_lines(content.splitlines())
    chunks = []

    for section in _iter_sections(lines):
        section_text = "\n".join(section["lines"]).strip()
        if not section_text:
            continue
        # 按空行分割段落
        paragraphs = re.split(r"\n\s*\n", section_text)
        raw_chunks = _split_paragraphs(paragraphs, max_chunk_len, overlap_chars)
        merged_chunks = _merge_small_chunks(raw_chunks, min_chunk_len, max_chunk_len)

        heading_path = " > ".join(section["header_path"]).strip()
        if not heading_path:
            heading_path = "未命名章节"

        for chunk in merged_chunks:
            chunks.append({
                "heading_path": heading_path,
                "start_line": section["start_line"],
                "content": chunk,
            })

    return chunks


def process_all_md_files():
    """批量处理 textbook/ 目录下的所有 .md 教材文件。

    输出：
    - chunks_result.json: 结构化分块（含文件来源、章节路径、行号）
    - chunks_preview.txt: 人类可读预览

    Returns:
        所有分块的列表。
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))
    textbook_dir = os.path.join(root_dir, "textbook")
    print(f"扫描目录：{textbook_dir}")

    # 列出目录内容
    print("\n目录里的所有文件：")
    for f in os.listdir(textbook_dir):
        print(f"  - {f}")

    # 筛选 .md 文件（排除 README）
    md_files = [
        f for f in os.listdir(textbook_dir)
        if f.endswith(".md") and f.lower() != "readme.md"
    ]

    if not md_files:
        print("\n未找到任何 Markdown 文件，请检查上面的文件列表！")
        return []

    print(f"\n找到 {len(md_files)} 个 MD 文件（已跳过 README）\n")

    all_chunks = []

    for filename in md_files:
        file_path = os.path.join(textbook_dir, filename)
        print(f"━━━━━━━━ 处理：{filename} ━━━━━━━━")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            chunks = split_markdown_by_headers(content)
            enriched_chunks = []
            for i, chunk in enumerate(chunks):
                enriched_chunks.append({
                    "file": filename,
                    "chunk_index": i + 1,
                    "heading_path": chunk["heading_path"],
                    "start_line": chunk["start_line"],
                    "content": chunk["content"],
                })
                preview = chunk["content"][:180].strip().replace("\n", " ")
                print(f"[{filename}] 块 {i + 1}：{preview}...")

            all_chunks.extend(enriched_chunks)
            print(f"{filename} 完成，共 {len(chunks)} 块\n")

        except Exception as e:
            print(f"出错：{str(e)}\n")

    print("=" * 50)
    print(f"全部处理完成")
    print(f"总文件数：{len(md_files)}")
    print(f"总分块数：{len(all_chunks)}")
    print("=" * 50)

    # 保存 JSON 结果
    json_path = os.path.join(root_dir, "chunks_result.json")
    txt_path = os.path.join(root_dir, "chunks_preview.txt")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    # 保存文本预览
    with open(txt_path, "w", encoding="utf-8") as f:
        for idx, item in enumerate(all_chunks):
            f.write(
                f"===== 块 {idx + 1} | 文件：{item['file']} | 章节：{item['heading_path']} =====\n"
            )
            f.write(item["content"])
            f.write("\n\n")

    print(f"分块已保存：")
    print(f"- {json_path}")
    print(f"- {txt_path}")

    return all_chunks


if __name__ == "__main__":
    process_all_md_files()
