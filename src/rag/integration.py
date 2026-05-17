"""
RAG 集成检索模块 —— 提供面向教学场景的增强版向量检索。

检索策略（混合评分）：
1. 向量相似度（余弦距离，权重 60%）
2. 词汇匹配度（关键词命中，权重 40%）
3. 学科加权（根据问题关键词推测学科，相关学科加权 1.0~1.5）
4. 无词汇匹配时额外惩罚 0.85x

使用方式：
    from rag.integration import retrieve_context
    context, sources = retrieve_context("什么是导数", top_k=3)
"""

import chromadb
import requests
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "math_knowledge_db")
COLLECTION_NAME = "math_textbooks_v2"

OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"

# ============================================================
# 学科关键词映射 —— 用于问题分类和学科加权
# ============================================================

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

# 文件名 → 学科映射（启动时自动构建）
FILE_SUBJECT_MAP = {}


def _build_file_subject_map():
    """根据 textbook/ 目录下的文件名自动构建学科映射。

    规则：
    - gaoshu* → 高等数学
    - discretemath* → 离散数学
    - linearalgebra* → 线性代数
    """
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

# ============================================================
# ChromaDB 连接管理
# ============================================================

_collection = None


def _get_collection():
    """获取 ChromaDB 集合（延迟初始化 + 连接缓存）。"""
    global _collection
    if _collection is not None:
        return _collection
    client = chromadb.PersistentClient(path=DB_PATH)
    _collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return _collection


# ============================================================
# 查询分析与向量化
# ============================================================

def _classify_query(query):
    """根据关键词匹配推测问题所属学科。

    Args:
        query: 用户问题文本

    Returns:
        [(学科名, 匹配关键词数), ...] 按匹配数降序排列。
    """
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
    """调用 Ollama API 获取文本的向量表示。

    Args:
        text: 待向量化的文本

    Returns:
        768 维浮点数向量列表。
    """
    res = requests.post(
        url=OLLAMA_EMBED_URL,
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=20,
    )
    res.raise_for_status()
    return res.json()["embedding"]


# ============================================================
# 词汇匹配辅助
# ============================================================

def _extract_terms(text):
    """从文本中提取检索词条。

    英文单词整体保留，中文按单字和双字 bigram 拆解，
    以支持向量检索外的词汇级别匹配。

    Args:
        text: 输入文本

    Returns:
        去重后的词条列表。
    """
    terms = re.findall(r"[A-Za-z0-9]+|[一-鿿]+", text)
    expanded = []
    for term in terms:
        if re.match(r"[一-鿿]+", term) and len(term) > 1:
            expanded.append(term)
            # 生成双字 bigram 用于部分匹配
            expanded.extend([term[i:i + 2] for i in range(len(term) - 1)])
        else:
            expanded.append(term.lower())
    return list(set(expanded))


def _strip_heading_prefix(doc):
    """去除文档开头的【章节】前缀标记。"""
    if not doc:
        return ""
    if doc.startswith("【章节】"):
        parts = doc.split("\n", 1)
        return parts[1] if len(parts) > 1 else ""
    return doc


def _lexical_score(query, doc, heading_path):
    """计算查询与文档之间的词汇匹配得分。

    英文词汇在正文中每次命中计 0.5 分，
    中文词汇每次命中计 1.0 分，
    标题命中额外加权 0.6x（中文）/ 0.3x（英文）。

    Args:
        query: 查询文本
        doc: 文档正文
        heading_path: 章节路径

    Returns:
        词汇匹配得分（浮点数）。
    """
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
    """从元数据中获取文档对应的学科分类。

    Args:
        meta: ChromaDB 元数据字典

    Returns:
        学科名称字符串。
    """
    fname = (meta or {}).get("file", "")
    return FILE_SUBJECT_MAP.get(fname, "未知")


# ============================================================
# 核心检索函数
# ============================================================

def search_knowledge(query_text, top_k=3):
    """增强版混合检索 —— 向量相似度 + 词汇匹配 + 学科加权。

    检索流程：
    1. 向量检索获取 top_k * 6 个候选
    2. 对每个候选计算综合评分（向量 60% + 词汇 40%）× 学科系数
    3. 按评分降序返回 top_k 个结果

    Args:
        query_text: 用户查询文本
        top_k: 返回的文档数量

    Returns:
        (context: str, sources: List[str])
        context 为拼接后的文档片段，sources 为来源信息列表。
    """
    collection = _get_collection()
    query_embedding = get_embedding(query_text)
    query_subjects = _classify_query(query_text)

    # 初次检索获取更多候选以提升召回率
    fetch_k = max(top_k * 6, top_k)
    try:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=fetch_k,
            include=["documents", "metadatas", "distances"],
        )
    except TypeError:
        # 兼容旧版 ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=fetch_k,
        )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    # 构建学科权重（匹配最多的学科权重为 1.5，其余线性缩放）
    subject_weight = {}
    max_subj_count = query_subjects[0][1] if query_subjects else 1
    for subj, count in query_subjects:
        subject_weight[subj] = 1.0 + (count / max_subj_count) * 0.5

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

        # 综合评分（向量 60% + 词汇 40%）× 学科系数
        score = (
            normalized_sim * 0.6
            + min(lexical / max(1, len(_extract_terms(query_text))), 1.0) * 0.4
        ) * subj_boost

        # 完全无词汇匹配时额外惩罚
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
    """检索与问题相关的教材上下文（供 model.py 调用）。

    Args:
        question: 用户问题
        top_k: 返回文档数

    Returns:
        (context: str, sources: List[str])
        数据库为空或检索失败时返回 ("", [])。
    """
    try:
        collection = _get_collection()
        if hasattr(collection, "count") and collection.count() == 0:
            return "", []
        context, sources = search_knowledge(question, top_k=top_k)
        return context, sources
    except Exception:
        return "", []
