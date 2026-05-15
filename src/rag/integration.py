import chromadb
import requests
import os

# ===================== 全局配置 =====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "math_knowledge_db")
COLLECTION_NAME = "math_textbooks"

# Ollama 接口地址（和视频里完全一致）
OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embeddings"
OLLAMA_CHAT_URL = "http://127.0.0.1:11434/api/generate"

# 模型配置
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "deepseek-r1:1.5b"  # 视频里的模型，你也可以换成其他 Ollama 模型

# ===================== 1. 初始化 Chroma 数据库 =====================
def init_chroma():
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return collection

# ===================== 2. 问题向量化 =====================
def get_embedding(text):
    res = requests.post(
        url=OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=20
    )
    return res.json()["embedding"]

# ===================== 3. 相似度检索教材内容 =====================
def search_knowledge(collection, query_text, top_k=3):
    query_embedding = get_embedding(query_text)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    # 拼接检索到的教材内容
    context = "\n\n".join([doc for doc in results["documents"][0]])
    sources = [meta["file"] for meta in results["metadatas"][0]]
    return context, sources

# ===================== 4. 调用 DeepSeek 回答问题 =====================
def ask_deepseek(question, context):
    # 构造 RAG 专用 Prompt，限制模型只能用教材内容回答
    prompt = f"""
你是一个数学助教，只能根据下面的教材内容回答用户问题。
如果教材里没有相关内容，就说“我暂时不知道，你可以问我教材里的知识点哦”。

【教材内容】
{context}

【用户问题】
{question}
"""

    res = requests.post(
        url=OLLAMA_CHAT_URL,
        json={
            "model": CHAT_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )
    return res.json()["response"]

# ===================== 5. 完整 RAG 问答流程 =====================
def math_qa(question):
    print(f"🔍 你的问题：{question}")
    # 1. 检索教材内容
    collection = init_chroma()
    context, sources = search_knowledge(collection, question)
    print(f"📚 参考教材：{', '.join(sources)}")

    # 2. 调用 DeepSeek 回答
    answer = ask_deepseek(question, context)
    print(f"\n🤖 回答：{answer}")
    return answer

# ===================== 运行 =====================
if __name__ == "__main__":
    # 示例提问（可以改成你自己的问题）
    math_qa("求导的基本公式是什么？")