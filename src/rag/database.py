"""
ChromaDB 数据库入库模块 —— 将向量化后的教材块批量写入 ChromaDB 向量数据库。

使用流程：
1. 读取 vectorized_chunks.json（由 embedding.py 生成）
2. 连接/创建 ChromaDB 持久化集合
3. 按 100 条一批批量插入（含文档文本、向量、元数据）
4. 可选测试检索验证数据质量

独立运行：python src/rag/database.py
"""

import json
import os
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from utils.encoding_setup import setup_windows_utf8
setup_windows_utf8()

import chromadb
import requests

# ============================================================
# 全局路径配置
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTOR_FILE = os.path.join(BASE_DIR, "vectorized_chunks.json")
DB_PATH = os.path.join(BASE_DIR, "db", "math_knowledge_db")
COLLECTION_NAME = "math_textbooks_v2"
OLLAMA_API = "http://127.0.0.1:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"


# ============================================================
# 数据读取
# ============================================================

def load_vectorized_data():
    """从 vectorized_chunks.json 读取已向量化的教材块数据。

    Returns:
        [{"file": str, "content": str, "embedding": [...], ...}, ...]
    """
    with open(VECTOR_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"读取到 {len(data)} 个向量化教材块")
    return data


# ============================================================
# 数据库初始化
# ============================================================

def init_chroma():
    """初始化 ChromaDB 持久化客户端并获取/创建集合。

    Returns:
        chromadb.Collection 实例。
    """
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    print(f"已连接到 Chroma 数据库：{COLLECTION_NAME}")
    return collection


def _build_document(item):
    """从数据项中提取文档文本（content 字段）。"""
    return item.get("content") or ""


def _file_to_subject(filename):
    """根据文件名判定学科分类。

    Args:
        filename: 教材文件名

    Returns:
        学科名称（高等数学 / 离散数学 / 线性代数 / 未知）。
    """
    lower = (filename or "").lower()
    if "gaoshu" in lower:
        return "高等数学"
    if "discretemath" in lower:
        return "离散数学"
    if "linearalgebra" in lower:
        return "线性代数"
    return "未知"


# ============================================================
# 批量插入
# ============================================================

def insert_data(collection, data):
    """将向量化教材数据批量插入 ChromaDB 集合。

    每批 100 条，每条包含：
    - id: UUID 唯一标识
    - document: 教材文本
    - embedding: 768 维向量
    - metadata: 文件来源、学科、章节路径、行号等

    Args:
        collection: ChromaDB 集合实例
        data: 向量化教材数据列表
    """
    print(f"准备插入 {len(data)} 个教材块...")
    batch_size = 100
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        ids = [str(uuid.uuid4()) for _ in batch]
        documents = [_build_document(item) for item in batch]
        embeddings = [item["embedding"] for item in batch]
        metadatas = [
            {
                "file": item["file"],
                "subject": _file_to_subject(item.get("file", "")),
                "heading_path": item.get("heading_path"),
                "chunk_index": item.get("chunk_index"),
                "start_line": item.get("start_line"),
            }
            for item in batch
        ]

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        print(f"已插入 {i + len(batch)}/{len(data)} 个块")
    print("\n所有数据已成功存入 Chroma 数据库！")


# ============================================================
# 向量化辅助（独立使用，不依赖 embedding.py）
# ============================================================

def ollama_embedding_by_api(text):
    """调用 Ollama API 对单条文本进行向量化。

    Args:
        text: 待向量化文本

    Returns:
        768 维浮点数向量列表，失败返回 None。
    """
    try:
        res = requests.post(
            url=OLLAMA_API,
            json={"model": MODEL_NAME, "prompt": text},
            timeout=20,
        )
        res.raise_for_status()
        return res.json()["embedding"]
    except Exception as e:
        print(f"向量化失败：{e}")
        return None


# ============================================================
# 检索测试
# ============================================================

def test_query(collection, query_text="求导的基本公式"):
    """用示例问题测试检索效果，验证入库数据质量。

    Args:
        collection: ChromaDB 集合实例
        query_text: 测试查询文本
    """
    print(f"\n测试检索：{query_text}")
    query_embedding = ollama_embedding_by_api(query_text)
    if not query_embedding:
        print("无法生成问题向量，终止检索")
        return

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
    )

    print("检索结果：")
    for i, doc in enumerate(results["documents"][0]):
        print(f"\n--- 结果 {i + 1} ---")
        print(f"来源文件：{results['metadatas'][0][i]['file']}")
        print(f"内容片段：{doc[:200]}...")


# ============================================================
# 主入口
# ============================================================

if __name__ == "__main__":
    vectorized_data = load_vectorized_data()
    collection = init_chroma()
    insert_data(collection, vectorized_data)
    test_query(collection)
