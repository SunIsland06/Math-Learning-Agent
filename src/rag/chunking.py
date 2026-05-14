import os
import sys
import io
import json

# 修复 Windows 打印乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def split_markdown_by_headers(content: str, max_chunk_len=1500):
    """
    按 Markdown 标题分段，保证知识点不被切断
    """
    lines = content.splitlines()
    chunks = []
    current_chunk = []
    current_len = 0

    for line in lines:
        line_stripped = line.strip()

        # 遇到标题自动新块
        if line_stripped.startswith(('# ', '## ', '### ')):
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                current_len = 0

        current_chunk.append(line)
        current_len += len(line)

        # 防止单块太长
        if current_len > max_chunk_len and len(current_chunk) > 2:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_len = 0

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks

def process_all_md_files():
    """
    修正版：扫描 rag/textbook/ 目录下的所有 .md 文件
    """
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
            all_chunks.extend([{"file": filename, "content": c} for c in chunks])

            for i, chunk in enumerate(chunks):
                preview = chunk[:180].encode("gbk", "ignore").decode("gbk").strip()
                print(f"[{filename}] 块 {i+1}：{preview}...")

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
            f.write(f"===== 块 {idx+1} | 文件：{item['file']} =====\n")
            f.write(item['content'])
            f.write("\n\n")

    print(f"💾 分块已保存：")
    print(f"- {json_path}")
    print(f"- {txt_path}")

    return all_chunks

if __name__ == "__main__":
    process_all_md_files()