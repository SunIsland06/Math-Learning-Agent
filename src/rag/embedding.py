import json
import requests
import os

# 配置（端口修正为11434，和视频一致）
OLLAMA_API = "http://127.0.0.1:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"

# 自动获取当前文件所在目录，不用手动改路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CHUNKS = os.path.join(BASE_DIR, "chunks_result.json")
OUTPUT_VECTORS = os.path.join(BASE_DIR, "vectorized_chunks.json")

def get_embedding(text):
    """调用 Ollama 生成向量"""
    # 向量化单条文本
    try:
        response = requests.post(
            OLLAMA_API,
            json={
                "model": MODEL_NAME,
                "prompt": text
            }
        )
        response.raise_for_status()  # 请求失败直接抛出错误
        return response.json()["embedding"]
    except Exception as e:
        print(f"❌ 向量生成失败：{e}")
        return None

def vectorize_all_chunks():
    # 批量读取分块并向量化
    # 读取分块结果
    with open(INPUT_CHUNKS, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"✅ 成功读取 {len(chunks)} 个文本块")
    print(f"✅ 开始向量化（使用 Ollama nomic-embed-text）...\n")

    vector_data = []

    for i, item in enumerate(chunks):
        file = item["file"]
        content = item["content"]

        print(f"[{i+1}/{len(chunks)}] 处理文件：{file}")

        emb = get_embedding(content)
        if emb:
            vector_data.append({
                "file": file,
                "content": content,
                "embedding": emb
            })

    # 保存带向量的数据
    with open(OUTPUT_VECTORS, "w", encoding="utf-8") as f:
        json.dump(vector_data, f, ensure_ascii=False, indent=2)

    print("\n========================================")
    print("✅ 全部向量化完成！")
    print(f"📦 结果已保存到：{OUTPUT_VECTORS}")
    print("========================================")

if __name__ == "__main__":
    vectorize_all_chunks()