"""
教材块向量化模块 —— 使用 Ollama 的 nomic-embed-text 模型将分块文本转为向量。

输入：chunks_result.json（由 chunking.py 生成）
输出：vectorized_chunks.json（含原始文本 + 768 维向量）

独立运行：python src/rag/embedding.py
"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from utils.encoding_setup import setup_windows_utf8
setup_windows_utf8()

import requests

# Ollama 本地嵌入服务配置
OLLAMA_API = "http://127.0.0.1:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"

# 基于当前文件路径自动解析输入/输出路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CHUNKS = os.path.join(BASE_DIR, "chunks_result.json")
OUTPUT_VECTORS = os.path.join(BASE_DIR, "vectorized_chunks.json")


def get_embedding(text):
    """调用 Ollama API 生成单条文本的向量表示。

    Args:
        text: 待向量化的文本内容

    Returns:
        768 维浮点数向量列表，失败返回 None。
    """
    try:
        response = requests.post(
            OLLAMA_API,
            json={"model": MODEL_NAME, "prompt": text},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["embedding"]
    except Exception as e:
        print(f"向量生成失败：{e}")
        return None


def _build_embedding_text(item):
    """从分块数据中提取用于向量化的文本（content 字段）。"""
    return item.get("content") or ""


def vectorize_all_chunks():
    """批量读取 chunks_result.json 中的所有分块，逐条向量化并保存。

    输出文件 vectorized_chunks.json 的每条记录包含：
    - file: 来源文件名
    - content: 原始文本
    - heading_path: 章节路径
    - chunk_index: 块序号
    - start_line: 起始行号
    - embedding: 768 维向量
    """
    with open(INPUT_CHUNKS, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"成功读取 {len(chunks)} 个文本块")
    print(f"开始向量化（使用 Ollama {MODEL_NAME}）...\n")

    vector_data = []

    for i, item in enumerate(chunks):
        file = item["file"]
        heading_path = item.get("heading_path")

        print(f"[{i + 1}/{len(chunks)}] 处理文件：{file}")

        emb_text = _build_embedding_text(item)
        emb = get_embedding(emb_text)
        if emb:
            vector_data.append({
                "file": file,
                "content": item["content"],
                "heading_path": heading_path,
                "chunk_index": item.get("chunk_index"),
                "start_line": item.get("start_line"),
                "embedding": emb,
            })

    # 保存带向量的完整数据
    with open(OUTPUT_VECTORS, "w", encoding="utf-8") as f:
        json.dump(vector_data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 40)
    print("全部向量化完成！")
    print(f"结果已保存到：{OUTPUT_VECTORS}")
    print("=" * 40)


if __name__ == "__main__":
    vectorize_all_chunks()
