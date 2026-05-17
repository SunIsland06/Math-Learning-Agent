"""
长期记忆管理器 —— 将用户对话向量化到 userdata/<username>/memory/，
新会话中检索相关历史记忆辅助回答。
"""
import json
import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import chromadb
import requests

# 配置
OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"
USERDATA_ROOT = Path(__file__).resolve().parents[2] / "userdata"


def _sanitize(name: str) -> str:
    return "".join(c for c in name if c.isalnum() or c in "-_.") or "unknown"


def _memory_db_path(username: str) -> str:
    safe = _sanitize(username)
    return str(USERDATA_ROOT / safe / "memory")


def _get_collection(username: str) -> chromadb.Collection:
    path = _memory_db_path(username)
    os.makedirs(path, exist_ok=True)
    client = chromadb.PersistentClient(path=path)
    return client.get_or_create_collection(name="conversation_memory")


def _embed(text: str) -> List[float]:
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

# ---- 词汇匹配辅助 ----
def _extract_terms(text: str) -> List[str]:
    terms = re.findall(r"[A-Za-z0-9]+|[一-鿿]+", text)
    expanded = []
    for term in terms:
        if re.match(r"[一-鿿]+", term) and len(term) > 1:
            expanded.append(term)
            expanded.extend([term[i:i+2] for i in range(len(term) - 1)])
        else:
            expanded.append(term.lower())
    return list(set(expanded))


def _lexical_score(query: str, doc: str) -> float:
    terms = _extract_terms(query)
    doc_lower = doc.lower()
    score = 0.0
    for term in terms:
        score += doc_lower.count(term.lower() if term.isascii() else term)
    return score


# ---- 公共 API ----

def store_memory(username: str, question: str, answer: str,
                 session_id: str = "", meta: Optional[Dict[str, Any]] = None) -> bool:
    """
    将一轮对话存储为长期记忆。
    自动向量化「问题 + 回答摘要」并写入 ChromaDB。
    """
    if not question or not answer:
        return False
    # 构建记忆文本：问题 + 回答前800字摘要
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
    """
    检索与当前问题相关的历史记忆。
    返回 [{"content": ..., "meta": ..., "score": ...}, ...]。
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
        normalized_sim = max(0.0, 1.0 - distance / 2.0)
        lexical = _lexical_score(query, doc)
        score = normalized_sim * 0.7 + min(lexical / max(1, len(_extract_terms(query))), 1.0) * 0.3
        candidates.append({
            "content": doc,
            "meta": metadatas[idx] if idx < len(metadatas) else {},
            "score": score,
        })

    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[:top_k]


def build_memory_message(username: str, query: str, top_k: int = 3) -> Optional[Dict[str, Any]]:
    """
    构建记忆系统消息（供 model.py 注入）。
    返回 None 表示无相关记忆。
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
