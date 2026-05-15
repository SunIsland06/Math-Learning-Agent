import json
import chromadb
import uuid
import os
import requests

# ===================== 全局配置 =====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTOR_FILE = os.path.join(BASE_DIR, "vectorized_chunks.json")
DB_PATH = os.path.join(BASE_DIR, "db", "math_knowledge_db")
COLLECTION_NAME = "math_textbooks"
OLLAMA_API = "http://127.0.0.1:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"

# ===================== 1. 读取向量化数据 =====================
def load_vectorized_data():
    with open(VECTOR_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"✅ 读取到 {len(data)} 个向量化教材块")
    return data

# ===================== 2. 初始化 Chroma 数据库 =====================
def init_chroma():
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    print(f"✅ 已连接到 Chroma 数据库：{COLLECTION_NAME}")
    return collection

# ===================== 3. 批量插入数据 =====================
def insert_data(collection, data):
    print(f"📦 准备插入 {len(data)} 个教材块...")
    batch_size = 100
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        ids = [str(uuid.uuid4()) for _ in batch]
        documents = [item["content"] for item in batch]
        embeddings = [item["embedding"] for item in batch]
        metadatas = [{"file": item["file"]} for item in batch]

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )
        print(f"✅ 已插入 {i+len(batch)}/{len(data)} 个块")
    print("\n🎉 所有数据已成功存入 Chroma 数据库！")

# ===================== 4. 内置向量化函数（不用导入） =====================
def ollama_embedding_by_api(text):
    try:
        res = requests.post(
            url=OLLAMA_API,
            json={
                "model": MODEL_NAME,
                "prompt": text
            },
            timeout=20
        )
        res.raise_for_status()
        return res.json()["embedding"]
    except Exception as e:
        print(f"❌ 向量化失败：{e}")
        return None

# ===================== 5. 测试检索 =====================
def test_query(collection, query_text="求导的基本公式"):
    print(f"\n🔍 测试检索：{query_text}")
    query_embedding = ollama_embedding_by_api(query_text)
    if not query_embedding:
        print("❌ 无法生成问题向量，终止检索")
        return

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print("📌 检索结果：")
    for i, doc in enumerate(results["documents"][0]):
        print(f"\n--- 结果 {i+1} ---")
        print(f"来源文件：{results['metadatas'][0][i]['file']}")
        print(f"内容片段：{doc[:200]}...")

# ===================== 运行 =====================
if __name__ == "__main__":
    # 1. 读取数据
    vectorized_data = load_vectorized_data()
    # 2. 初始化数据库
    collection = init_chroma()
    # 3. 插入数据（如果已经插入过，注释掉这行即可）
    insert_data(collection, vectorized_data)
    # 4. 测试检索
    test_query(collection)