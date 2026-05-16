import chromadb
import requests
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "math_knowledge_db")
COLLECTION_NAME = "math_textbooks_v2"

OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"

# ---- 学科关键词映射 ----
SUBJECT_KEYWORDS = {
    "高等数学": [
        "极限", "导数", "微分", "积分", "级数", "偏导", "重积分", "曲线积分",
        "曲面积分", "无穷", "连续", "可导", "泰勒", "麦克劳林", "洛必达",
        "不定积分", "定积分", "原函数", "方向导数", "梯度", "散度", "旋度",
        "傅里叶", "幂级数", "收敛", "发散", "微分方程", "通解", "特解",
        "中值定理", "极值", "最值", "切线", "法线", "曲率", "弧长",
        "二重积分", "三重积分", "格林", "高斯", "斯托克斯",
    ],
    "线性代数": [
        "矩阵", "行列式", "向量", "线性", "特征值", "特征向量", "二次型",
        "方程组", "秩", "逆矩阵", "正交", "对角化", "线性空间", "子空间",
        "线性变换", "基", "维数", "解空间", "齐次", "非齐次", "伴随矩阵",
        "转置", "对称矩阵", "正定", "单位矩阵", "初等变换", "行阶梯",
        "克拉默", "相似", "合同", "施密特", "正交基", "标准型",
    ],
    "离散数学": [
        "集合", "关系", "图", "树", "逻辑", "命题", "谓词", "组合",
        "计数", "递推", "布尔", "格", "代数系统", "群", "环", "域",
        "等价", "偏序", "全序", "映射", "单射", "满射", "双射",
        "连通", "通路", "回路", "哈密顿", "欧拉", "平面图", "着色",
        "生成树", "最短路径", "前缀码", "自动机", "文法", "语言",
        "归纳", "递归", "排列", "组合数", "容斥", "鸽巢",
    ],
}

# 文件名 → 学科映射
FILE_SUBJECT_MAP = {}

def _build_file_subject_map():
    global FILE_SUBJECT_MAP
    textbook_dir = os.path.join(BASE_DIR, "textbook")
    if not os.path.isdir(textbook_dir):
        return
    for fname in os.listdir(textbook_dir):
        if not fname.endswith(".md"):
            continue
        lower = fname.lower()
        if "gaoshu" in lower:
            FILE_SUBJECT_MAP[fname] = "高等数学"
        elif "discretemath" in lower:
            FILE_SUBJECT_MAP[fname] = "离散数学"
        elif "linearalgebra" in lower:
            FILE_SUBJECT_MAP[fname] = "线性代数"
        else:
            FILE_SUBJECT_MAP[fname] = "未知"

_build_file_subject_map()

# ---- ChromaDB 连接缓存 ----
_collection = None

def _get_collection():
    global _collection
    if _collection is not None:
        return _collection
    client = chromadb.PersistentClient(path=DB_PATH)
    _collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return _collection


def _classify_query(query):
    """根据关键词匹配，返回 [(学科, 匹配数), ...] 降序排列。"""
    scores = {}
    query_lower = query.lower()
    for subject, keywords in SUBJECT_KEYWORDS.items():
        count = 0
        for kw in keywords:
            if kw in query or kw.lower() in query_lower:
                count += 1
        if count > 0:
            scores[subject] = count
    if not scores:
        return []
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def get_embedding(text):
    res = requests.post(
        url=OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=20
    )
    res.raise_for_status()
    return res.json()["embedding"]


def _extract_terms(text):
    terms = re.findall(r"[A-Za-z0-9]+|[一-鿿]+", text)
    expanded = []
    for term in terms:
        if re.match(r"[一-鿿]+", term) and len(term) > 1:
            expanded.append(term)
            expanded.extend([term[i:i+2] for i in range(len(term) - 1)])
        else:
            expanded.append(term.lower())
    return list(set(expanded))


def _strip_heading_prefix(doc):
    if not doc:
        return ""
    if doc.startswith("【章节】"):
        parts = doc.split("\n", 1)
        return parts[1] if len(parts) > 1 else ""
    return doc


def _lexical_score(query, doc, heading_path):
    terms = _extract_terms(query)
    doc_body = _strip_heading_prefix(doc)
    doc_text = (doc_body or "").lower()
    heading_text = (heading_path or "").lower()
    score = 0.0
    for term in terms:
        if term.isascii():
            score += doc_text.count(term) * 0.5
        else:
            score += (doc_body or "").count(term) * 1.0
    # 标题命中加权
    if heading_text:
        for term in terms:
            if term.isascii():
                score += heading_text.count(term) * 0.3
            else:
                score += (heading_path or "").count(term) * 0.6
    return score


def _subject_of_meta(meta):
    """从元数据中获取文件对应的学科。"""
    fname = (meta or {}).get("file", "")
    return FILE_SUBJECT_MAP.get(fname, "未知")


def search_knowledge(query_text, top_k=3):
    """
    改进版检索：向量相似度 + 词汇匹配 + 学科加权。
    """
    collection = _get_collection()
    query_embedding = get_embedding(query_text)
    query_subjects = _classify_query(query_text)

    fetch_k = max(top_k * 6, top_k)
    try:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=fetch_k,
            include=["documents", "metadatas", "distances"]
        )
    except TypeError:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=fetch_k
        )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    # 构建查询学科权重
    subject_weight = {}
    max_subj_count = query_subjects[0][1] if query_subjects else 1
    for subj, count in query_subjects:
        subject_weight[subj] = 1.0 + (count / max_subj_count) * 0.5  # 1.0 ~ 1.5

    candidates = []
    for idx, doc in enumerate(documents):
        meta = metadatas[idx] if idx < len(metadatas) else {}
        heading_path = meta.get("heading_path", "")
        distance = distances[idx] if idx < len(distances) else 1.0
        doc_subject = _subject_of_meta(meta)

        # 余弦距离归一化到 [0, 1]（ChromaDB cosine dist 范围为 [0, 2]）
        normalized_sim = max(0.0, 1.0 - distance / 2.0)

        lexical = _lexical_score(query_text, doc, heading_path)

        # 学科加权
        subj_boost = subject_weight.get(doc_subject, 0.85)

        # 综合评分：向量相似度 60% + 词汇匹配 40%，再乘以学科系数
        score = (normalized_sim * 0.6 + min(lexical / max(1, len(_extract_terms(query_text))), 1.0) * 0.4) * subj_boost

        # 完全无词汇匹配的轻微惩罚
        if lexical == 0:
            score *= 0.85

        candidates.append({
            "doc": doc,
            "meta": meta,
            "score": score,
            "subject": doc_subject,
            "heading": heading_path,
        })

    candidates.sort(key=lambda item: item["score"], reverse=True)
    top_hits = candidates[:top_k]

    context = "\n\n".join([item["doc"] for item in top_hits])
    sources = [
        f"{item['meta'].get('file')} | {item['subject']} | {item['heading']}"
        for item in top_hits
    ]
    return context, sources


def retrieve_context(question, top_k=3):
    """Return (context, sources) for the given question, or ("", [])."""
    try:
        collection = _get_collection()
        if hasattr(collection, "count") and collection.count() == 0:
            return "", []
        context, sources = search_knowledge(question, top_k=top_k)
        return context, sources
    except Exception:
        return "", []
