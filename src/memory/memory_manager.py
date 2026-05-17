"""
长期记忆管理器 —— 将用户对话向量化存储到 ChromaDB，新会话中检索相关历史。

工作机制：
1. store_memory() — 对话结束后将问答对向量化存入 userdata/<username>/memory/
2. retrieve_memories() — 新问题时检索历史相关记忆（向量相似度 + 词汇匹配）
3. build_memory_message() — 构建注入到 LLM 对话的 system 消息

每个用户的记忆独立存储，通过 ChromaDB 持久化。
"""

import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import chromadb
import requests

# ============================================================
# 配置
# ============================================================

OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"
USERDATA_ROOT = Path(__file__).resolve().parents[2] / "userdata"


def _sanitize(name: str) -> str:
    """过滤用户名中的非法字符，防止路径穿越。"""
    return "".join(c for c in name if c.isalnum() or c in "-_.") or "unknown"


def _memory_db_path(username: str) -> str:
    """获取用户记忆数据库路径。"""
    safe = _sanitize(username)
    return str(USERDATA_ROOT / safe / "memory")


def _get_collection(username: str) -> chromadb.Collection:
    """获取用户的 ChromaDB 记忆集合（自动创建目录和集合）。"""
    path = _memory_db_path(username)
    os.makedirs(path, exist_ok=True)
    client = chromadb.PersistentClient(path=path)
    return client.get_or_create_collection(name="conversation_memory")


def _embed(text: str) -> List[float]:
    """调用 Ollama 将文本转为向量。

    Args:
        text: 待嵌入文本

    Returns:
        768 维向量列表，失败返回空列表。
    """
    try:
        res = requests.post(
            OLLAMA_EMBED_URL,
            json={"model": EMBED_MODEL, "prompt": text},
            timeout=20,
        )
        res.raise_for_status()
        return res.json()["embedding"]
    except Exception:
        return []


# ============================================================
# 词汇匹配辅助
# ============================================================

def _extract_terms(text: str) -> List[str]:
    """从文本中提取检索词条（中文 bigram + 英文单词）。"""
    terms = re.findall(r"[A-Za-z0-9]+|[一-鿿]+", text)
    expanded = []
    for term in terms:
        if re.match(r"[一-鿿]+", term) and len(term) > 1:
            expanded.append(term)
            expanded.extend([term[i:i + 2] for i in range(len(term) - 1)])
        else:
            expanded.append(term.lower())
    return list(set(expanded))


def _lexical_score(query: str, doc: str) -> float:
    """计算查询与记忆文档的词汇匹配得分。

    Args:
        query: 当前查询文本
        doc: 记忆文档文本

    Returns:
        词汇匹配得分（浮点数）。
    """
    terms = _extract_terms(query)
    doc_lower = doc.lower()
    score = 0.0
    for term in terms:
        score += doc_lower.count(term.lower() if term.isascii() else term)
    return score


# ============================================================
# 公共 API
# ============================================================

def store_memory(username: str, question: str, answer: str,
                 session_id: str = "", meta: Optional[Dict[str, Any]] = None) -> bool:
    """将一轮问答存入用户的长期记忆。

    记忆文本 = "Q: 问题前500字\nA: 回答前800字摘要"
    自动向量化后写入 ChromaDB。

    Args:
        username: 用户名
        question: 用户问题
        answer: AI 回答
        session_id: 会话 ID
        meta: 额外元数据

    Returns:
        True 表示存储成功，False 表示失败。
    """
    if not question or not answer:
        return False

    # 构建记忆文本：问题 + 回答摘要
    summary = answer[:800] if len(answer) > 800 else answer
    memory_text = f"Q: {question[:500]}\nA: {summary}"
    embedding = _embed(memory_text)
    if not embedding:
        return False

    try:
        collection = _get_collection(username)
        meta_data = {
            "session_id": str(session_id),
            "question": question[:300],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        if meta:
            meta_data.update(meta)
        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[memory_text],
            embeddings=[embedding],
            metadatas=[meta_data],
        )
        return True
    except Exception:
        return False


def retrieve_memories(username: str, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
    """检索与当前问题相关的历史记忆。

    采用混合评分：向量相似度 70% + 词汇匹配 30%。

    Args:
        username: 用户名
        query: 当前查询文本
        top_k: 返回的记忆数量

    Returns:
        [{"content": str, "meta": dict, "score": float}, ...]
    """
    collection = _get_collection(username)
    try:
        count = collection.count()
    except Exception:
        count = 0
    if count == 0:
        return []

    query_embedding = _embed(query)
    if not query_embedding:
        return []

    # 检索更多候选以提升召回率
    fetch_k = min(count, max(top_k * 4, top_k))
    try:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=fetch_k,
            include=["documents", "metadatas", "distances"],
        )
    except TypeError:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=fetch_k,
        )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    candidates = []
    for idx, doc in enumerate(documents):
        distance = distances[idx] if idx < len(distances) else 1.0
        # 余弦距离 → 相似度（距离范围 [0, 2]）
        normalized_sim = max(0.0, 1.0 - distance / 2.0)
        lexical = _lexical_score(query, doc)
        # 综合评分：向量 70% + 词汇 30%
        score = normalized_sim * 0.7 + min(lexical / max(1, len(_extract_terms(query))), 1.0) * 0.3
        candidates.append({
            "content": doc,
            "meta": metadatas[idx] if idx < len(metadatas) else {},
            "score": score,
        })

    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[:top_k]


def build_memory_message(username: str, query: str, top_k: int = 3) -> Optional[Dict[str, Any]]:
    """构建注入 LLM 对话的记忆 system 消息。

    Args:
        username: 用户名
        query: 当前查询文本
        top_k: 最大记忆数

    Returns:
        {"role": "system", "content": "..."} 或 None（无相关记忆时）。
    """
    if not username:
        return None
    memories = retrieve_memories(username, query, top_k=top_k)
    if not memories:
        return None

    lines = [
        "【长期记忆】以下是用户之前相关学习对话的记忆片段，可参考这些信息辅助回答：",
        "",
    ]
    for i, m in enumerate(memories, 1):
        meta = m.get("meta", {})
        ts = meta.get("timestamp", "")[:10]
        lines.append(f"记忆 {i}（{ts}）:")
        lines.append(m["content"])
        lines.append("")

    content = "\n".join(lines)
    return {"role": "system", "content": content}
