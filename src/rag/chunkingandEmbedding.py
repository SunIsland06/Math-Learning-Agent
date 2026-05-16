import json
import requests
import os

# 【关键修正：端口改为 11434】
OLLAMA_API = "http://127.0.0.1:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHUNK_FILE = os.path.join(BASE_DIR, "chunks_result.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "vectorized_chunks.json")

def file_chunk_list():
    # 读取分块结果
    with open(CHUNK_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    return chunks

def ollama_embedding_by_api(text):
    # 调用 Ollama 生成向量
    try:
        res = requests.post(
            url=OLLAMA_API,
            json={
                "model": MODEL_NAME,
                "prompt": text
            },
            timeout=15
        )
        res.raise_for_status()
        return res.json()["embedding"]
    except Exception as e:
        print(f"❌ 向量化失败：{e}")
        return None

def run():
    # 批量向量化并写入输出文件
    print("✅ 开始读取教材分块...")
    chunks = file_chunk_list()
    print(f"✅ 共加载 {len(chunks)} 个教材知识点块\n")

    print("=" * 60)
    print("开始向量化（nomic-embed-text）")
    print("=" * 60)

    vectorized_data = []
    for i, item in enumerate(chunks):
        print(f"\n📦 处理第 {i+1}/{len(chunks)} 个教材块：{item['file']}")
        vector = ollama_embedding_by_api(item["content"])
        if vector:
            vectorized_data.append({
                "file": item["file"],
                "content": item["content"],
                "embedding": vector
            })
            print(f"✅ 向量长度：{len(vector)}")

    # 保存带向量的数据
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(vectorized_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 全部完成！结果已保存到：{OUTPUT_FILE}")

if __name__ == '__main__':
    run()