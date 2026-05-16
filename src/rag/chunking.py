import os
import sys
import io
import json
import re

# 修复 Windows 打印乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)$")
IMAGE_RE = re.compile(r"^!\[.*?\]\(.*?\)\s*$")

DEFAULT_MAX_CHARS = 1000
DEFAULT_OVERLAP_CHARS = 120
DEFAULT_MIN_CHARS = 200

def _clean_lines(lines):
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
                    "lines": current
                }
                current = []
            level = len(match.group(1))
            title = match.group(2).strip() or "未命名章节"
            if len(headers) >= level:
                headers = headers[: level - 1]
            headers.append(title)
            start_line = idx
        current.append(line)

    if current:
        yield {
            "header_path": headers[:],
            "start_line": start_line,
            "lines": current
        }

def _split_paragraphs(paragraphs, max_chars, overlap_chars):
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

def split_markdown_by_headers(content: str, max_chunk_len=DEFAULT_MAX_CHARS, overlap_chars=DEFAULT_OVERLAP_CHARS, min_chunk_len=DEFAULT_MIN_CHARS):
    """
    按 Markdown 标题分段，再按段落切块，避免长段落断裂。
    """
    lines = _clean_lines(content.splitlines())
    chunks = []

    for section in _iter_sections(lines):
        section_text = "\n".join(section["lines"]).strip()
        if not section_text:
            continue
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
                "content": chunk
            })

    return chunks

def process_all_md_files():
    """
    修正版：扫描 rag/textbook/ 目录下的所有 .md 文件
    """
    # 关键修正：指定到 textbook 子目录
    # 关键修正：指定到 textbook 子目录
    root_dir = os.path.dirname(os.path.abspath(__file__))
    textbook_dir = os.path.join(root_dir, "textbook")
    print(f"📂 扫描目录：{textbook_dir}")

    # 先打印目录里所有文件，帮你排查问题
    print("\n📋 目录里的所有文件：")
    for f in os.listdir(textbook_dir):
        print(f"  - {f}")

    # 找出所有 .md 文件，排除 README.md
    md_files = [
        f for f in os.listdir(textbook_dir)
        if f.endswith(".md") and f.lower() != "readme.md"
    ]

    if not md_files:
        print("\n❌ 未找到任何 Markdown 文件，请检查上面的文件列表！")
        return []

    print(f"\n✅ 找到 {len(md_files)} 个 MD 文件（已跳过 README）\n")

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
                    "content": chunk["content"]
                })
                preview = chunk["content"][:180].encode("gbk", "ignore").decode("gbk").strip()
                print(f"[{filename}] 块 {i+1}：{preview}...")

            all_chunks.extend(enriched_chunks)

            print(f"✅ {filename} 完成，共 {len(chunks)} 块\n")

        except Exception as e:
            print(f"❌ 出错：{str(e)}\n")

    print("=" * 50)
    print(f"📦 全部处理完成")
    print(f"总文件数：{len(md_files)}")
    print(f"总分块数：{len(all_chunks)}")
    print("=" * 50)

    # 保存结果到 rag 目录下
    json_path = os.path.join(root_dir, "chunks_result.json")
    txt_path = os.path.join(root_dir, "chunks_preview.txt")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    with open(txt_path, "w", encoding="utf-8") as f:
        for idx, item in enumerate(all_chunks):
            f.write(
                f"===== 块 {idx+1} | 文件：{item['file']} | 章节：{item['heading_path']} =====\n"
            )
            f.write(item["content"])
            f.write("\n\n")

    print(f"💾 分块已保存：")
    print(f"- {json_path}")
    print(f"- {txt_path}")

    return all_chunks

if __name__ == "__main__":
    process_all_md_files()