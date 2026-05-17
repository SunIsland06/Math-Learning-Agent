"""
Flask Web 应用主模块 —— 数学学习助手的 Web 入口。

提供用户认证（注册/登录/登出）、会话管理（创建/列表/删除）、
文件上传、以及基于 SSE 流式输出的 AI 问答接口。
通过 MySQL 持久化用户、会话和消息数据。
"""

from datetime import datetime, timezone
import hashlib
import re
import sys
from pathlib import Path

from flask import (
    Flask,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    stream_with_context,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy

# 将 src 根目录加入模块搜索路径，便于跨目录导入
sys.path.append(str(Path(__file__).resolve().parents[1]))
from model.model import Model
from mcp_services.mcp_manager import get_mcp_manager
from utils.user_config import load_config, save_config
from utils.document_parser import parse_document
from memory.memory_manager import store_memory

app = Flask(__name__)
app.secret_key = "123456789"

# MySQL 数据库连接配置（使用 PyMySQL 驱动）
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:672284Aa.@127.0.0.1:3306/flask_chat?charset=utf8mb4"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 用户数据根目录（附件、记忆、个人配置）
USERDATA_ROOT = Path(__file__).resolve().parents[2] / "userdata"

db = SQLAlchemy(app)


# ============================================================
# 数据模型定义
# ============================================================

class User(db.Model):
    """用户信息表 —— 存储注册用户的账号与加密密码。"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class ChatRecord(db.Model):
    """简易问答记录表 —— 存储单轮问答的完整记录（用于首页历史展示）。"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)


class ChatSession(db.Model):
    """会话表 —— 每个会话包含多轮对话消息。"""
    __tablename__ = "chat_session"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ChatMessage(db.Model):
    """会话消息表 —— 存储会话中的每条消息（system/user/assistant）。"""
    __tablename__ = "chat_message"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    session_id = db.Column(db.BigInteger, nullable=False, index=True)
    role = db.Column(db.Enum("system", "user", "assistant"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    seq = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# ============================================================
# 工具函数
# ============================================================

def sha256_encrypt(pwd: str) -> str:
    """对密码进行 SHA-256 哈希加密。"""
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()


def generate_title(question: str) -> str:
    """根据用户首条问题截取会话标题（最长15字符）。"""
    text = (question or "").strip()
    if not text:
        return f"new-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}"
    return text[:15]


def sanitize_path_part(value: str) -> str:
    """过滤路径中的非法字符，仅保留字母数字、点号、下划线和连字符。"""
    return re.sub(r"[^a-zA-Z0-9._-]", "_", value or "")


def get_user_session_dir(username: str, session_id: str | int, ensure: bool = True) -> Path:
    """获取用户会话的附件存储目录，ensure=True 时自动创建。"""
    safe_user = sanitize_path_part(str(username))
    safe_session = sanitize_path_part(str(session_id))
    target = USERDATA_ROOT / safe_user / safe_session
    if ensure:
        target.mkdir(parents=True, exist_ok=True)
    return target


def build_attachment_context(attachments, username: str, session_id: str | int):
    """为模型生成附件上下文文本和图片数据 —— 解析文件内容注入消息。

    Args:
        attachments: 前端传来的附件元数据列表
        username: 当前用户名
        session_id: 当前会话 ID

    Returns:
        (text_context: str, image_data_list: list)
        text_context: 格式化的文本上下文字符串
        image_data_list: [(name, data_uri), ...] 图片的 Base64 Data URI 列表
    """
    if not attachments:
        return "", []

    lines = []
    image_data_list = []
    base_dir = get_user_session_dir(username, session_id, ensure=False)

    for item in attachments:
        if not isinstance(item, dict):
            continue
        name = (item.get("name") or "").strip()
        stored_name = (item.get("stored_name") or "").strip()
        kind = (item.get("kind") or "file").strip()
        if not stored_name:
            continue
        safe_name = Path(stored_name).name
        file_path = base_dir / safe_name
        if not file_path.exists():
            continue
        url = f"/userdata/{sanitize_path_part(username)}/{sanitize_path_part(str(session_id))}/{safe_name}"

        if kind == "markdown" or safe_name.lower().endswith(".md"):
            text, _ = parse_document(str(file_path), "markdown")
            if len(text) > 4000:
                text = text[:4000] + "\n...[truncated]"
            lines.append(f"[Markdown 文件: {name}]\n```\n{text}\n```")

        elif kind == "image":
            # 使用文档解析器获取图片 Base64 编码（供视觉模型识别）
            prompt, data_uri = parse_document(str(file_path), "image")
            image_data_list.append((name, data_uri))
            # 同时提供文本提示和 URL
            lines.append(
                f"[图片: {name}]\nURL: {url}\n"
                f"（图片已提交视觉识别，模型将自动分析图片内容）"
            )

        elif kind == "document" or safe_name.lower().endswith((".pdf", ".doc", ".docx")):
            doc_type = "pdf" if safe_name.lower().endswith(".pdf") else "docx"
            text, _ = parse_document(str(file_path), doc_type)
            if len(text) > 6000:
                text = text[:6000] + "\n...[truncated]"
            lines.append(f"[文档: {name}]\nURL: {url}\n内容：\n{text}")

        else:
            lines.append(f"[文件: {name}]\nURL: {url}")

    if not lines and not image_data_list:
        return "", []

    text_context = "附件如下：\n" + "\n\n".join(lines) if lines else ""
    return text_context, image_data_list


def build_attachment_markdown(attachments, username: str, session_id: str | int) -> str:
    """为消息存储生成附件的 Markdown 表示 —— 图片用 ![]() 语法，文件用链接。"""
    if not attachments:
        return ""

    base_dir = get_user_session_dir(username, session_id, ensure=False)
    lines = []
    for item in attachments:
        if not isinstance(item, dict):
            continue
        name = (item.get("name") or "").strip() or "attachment"
        stored_name = (item.get("stored_name") or "").strip()
        if not stored_name:
            continue
        safe_name = Path(stored_name).name
        file_path = base_dir / safe_name
        if not file_path.exists():
            continue
        url = f"/userdata/{sanitize_path_part(username)}/{sanitize_path_part(str(session_id))}/{safe_name}"

        if safe_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            lines.append(f"![{name}]({url})")
        else:
            lines.append(f"[{name}]({url})")

    if not lines:
        return ""

    return "\n\n".join(lines)


def get_ai_answer_with_messages_stream(
    messages,
    question,
    enable_thinking=False,
    thinking_strength="high",
    search=False,
    memory=False,
    username="",
    session_id="",
    image_data_list=None,
):
    """组装模型上下文并通过生成器流式输出 AI 回答。

    Args:
        messages: 历史对话消息列表
        question: 当前用户问题
        enable_thinking: 是否启用深度思考（显示推理过程）
        thinking_strength: 思考强度（"high" / "low"）
        search: 是否启用联网搜索
        memory: 是否启用长期记忆
        username: 当前用户名
        session_id: 当前会话 ID
        image_data_list: [(name, data_uri), ...] 图片附件列表

    Yields:
        SSE 文本块（逐 token 输出）。
    """
    model = Model()
    # 设置输出目录用于技能生成的图片持久化
    if username and session_id:
        output_dir = get_user_session_dir(username, session_id, ensure=True)
        model.skill_caller.context = {
            "output_dir": str(output_dir),
            "output_url_prefix": f"/userdata/{sanitize_path_part(username)}/{sanitize_path_part(str(session_id))}/",
        }
    # 注入历史消息（保留系统提示词在首位）
    model.messages = model.messages[:1] + messages
    model.enable_thinking = enable_thinking
    model.thinking_strength = thinking_strength
    model.enable_search = search
    model.enable_memory = memory
    model.memory_username = username
    yield from model.stream_chat_chunks(question, image_data_list=image_data_list or [])


# ============================================================
# 用户认证路由
# ============================================================

@app.route("/register", methods=["GET", "POST"])
def register():
    """用户注册 —— GET 返回注册页面，POST 处理注册表单。"""
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        pwd_confirm = request.form.get("pwd_confirm")
        if pwd != pwd_confirm:
            return "两次密码不一致！<a href='/register'>返回注册</a>"
        if User.query.filter_by(username=username).first():
            return "账号已存在！<a href='/register'>返回注册</a>"
        encrypt_pwd = sha256_encrypt(pwd)
        db.session.add(User(username=username, password=encrypt_pwd))
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """用户登录 —— GET 返回登录页面，POST 验证账号密码并写入 session。"""
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        user = User.query.filter_by(username=username).first()
        if not user:
            return "账号或密码错误！<a href='/login'>重新登录</a>"
        if sha256_encrypt(pwd) == user.password:
            session["username"] = username
            return redirect(url_for("index"))
        return "账号或密码错误！<a href='/login'>重新登录</a>"
    return render_template("login.html")


@app.route("/logout")
def logout():
    """退出登录 —— 清除 session 并重定向到登录页。"""
    session.clear()
    return redirect(url_for("login"))


# ============================================================
# 用户设置路由
# ============================================================

@app.route("/settings/load", methods=["GET"])
def settings_load():
    """加载当前用户的个人设置（思考开关、搜索开关等）。"""
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401
    return jsonify(load_config(username))


@app.route("/settings/save", methods=["POST"])
def settings_save():
    """保存当前用户的个人设置到 userdata/<username>/config.yml。"""
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401
    data = request.get_json() or {}
    save_config(username, data)
    return jsonify({"ok": True})


# ============================================================
# 首页与静态文件路由
# ============================================================

@app.route("/")
def index():
    """首页 —— 展示当前用户的历史问答记录。"""
    if "username" not in session:
        return redirect(url_for("login"))
    history = ChatRecord.query.filter_by(username=session["username"]).all()
    return render_template("index.html", username=session["username"], history=history)


@app.route("/userdata/<username>/<session_id>/<path:filename>")
def userdata_files(username, session_id, filename):
    """静态附件下载 —— 从用户会话目录提供文件服务。"""
    safe_user = sanitize_path_part(username)
    safe_session = sanitize_path_part(session_id)
    base_dir = USERDATA_ROOT / safe_user / safe_session
    return send_from_directory(base_dir, filename, as_attachment=False)


# ============================================================
# 会话管理路由
# ============================================================

@app.route("/session/new", methods=["POST"])
def session_new():
    """新建会话 —— 在数据库中创建空会话并返回 session_id。"""
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401
    new_session = ChatSession(username=username, title="new")
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"session_id": new_session.id})


@app.route("/session/list", methods=["GET"])
def session_list():
    """获取当前用户的会话列表（按更新时间降序）。"""
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401
    rows = (
        ChatSession.query.filter_by(username=username)
        .order_by(ChatSession.updated_at.desc())
        .all()
    )
    return jsonify([{"session_id": row.id, "title": row.title} for row in rows])


@app.route("/session/messages", methods=["GET"])
def session_messages():
    """获取指定会话的完整消息历史（含角色和内容）。"""
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401

    session_id = request.args.get("session_id")
    if not session_id:
        return jsonify({"error": "session_id_required"}), 400

    row = ChatSession.query.filter_by(id=session_id, username=username).first()
    if not row:
        return jsonify({"error": "session_not_found"}), 404

    messages = (
        ChatMessage.query.filter_by(session_id=row.id)
        .order_by(ChatMessage.seq.asc())
        .all()
    )
    return jsonify(
        {
            "session_id": row.id,
            "title": row.title,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
        }
    )


@app.route("/session/title", methods=["POST"])
def session_title():
    """更新会话标题（最长15字符）。"""
    data = request.get_json() or {}
    session_id = data.get("session_id")
    title = (data.get("title") or "").strip()[:15]
    row = ChatSession.query.filter_by(
        id=session_id, username=session.get("username", "")
    ).first()
    if not row:
        return jsonify({"error": "not_found"}), 404
    row.title = title or row.title
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/session/delete", methods=["POST"])
def session_delete():
    """删除会话及其所有关联消息。"""
    data = request.get_json() or {}
    session_id = data.get("session_id")
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401

    row = ChatSession.query.filter_by(id=session_id, username=username).first()
    if not row:
        return jsonify({"error": "not_found"}), 404

    ChatMessage.query.filter_by(session_id=row.id).delete()
    db.session.delete(row)
    db.session.commit()
    return jsonify({"ok": True})


# ============================================================
# 文件上传路由
# ============================================================

@app.route("/upload", methods=["POST"])
def upload():
    """上传附件并保存到用户会话目录。

    支持的文件类型：图片（png/jpg/jpeg/webp）、Markdown（.md）、
    以及常见文档格式（pdf/doc/docx/ppt/pptx）。
    """
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401

    session_id = request.form.get("session_id", "").strip()
    if not session_id:
        return jsonify({"error": "session_id_required"}), 400

    row = ChatSession.query.filter_by(id=session_id, username=username).first()
    if not row:
        return jsonify({"error": "session_not_found"}), 404

    if "file" not in request.files:
        return jsonify({"error": "file_required"}), 400

    file = request.files["file"]
    if not file or not file.filename:
        return jsonify({"error": "file_required"}), 400

    # 过滤扩展名，防止上传可执行文件
    original_name = Path(file.filename).name
    ext = Path(original_name).suffix.lower()
    allowed_ext = {".png", ".jpg", ".jpeg", ".webp", ".md", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".word", ".ppt"}
    if ext not in allowed_ext:
        return jsonify({"error": "unsupported_type"}), 400

    # 生成安全的存储文件名（时间戳 + 原始扩展名）
    safe_stem = sanitize_path_part(Path(original_name).stem) or "upload"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
    stored_name = f"{safe_stem}-{stamp}{ext}"
    target_dir = get_user_session_dir(username, session_id, ensure=True)
    target_path = target_dir / stored_name
    file.save(target_path)

    # 按扩展名分类：image / markdown / document
    kind = "image" if ext in {".png", ".jpg", ".jpeg", ".webp"} else "markdown" if ext == ".md" else "document"
    url = f"/userdata/{sanitize_path_part(username)}/{sanitize_path_part(str(session_id))}/{stored_name}"

    return jsonify(
        {
            "name": original_name,
            "stored_name": stored_name,
            "url": url,
            "kind": kind,
            "ext": ext,
        }
    )


# ============================================================
# 核心问答路由（SSE 流式输出）
# ============================================================

@app.route("/ask", methods=["POST"])
def ask():
    """主问答接口 —— 接收用户问题，通过 SSE 流式返回 AI 回答。

    处理流程：
    1. 验证用户登录状态
    2. 读取用户个人设置（思考/搜索/记忆开关）
    3. 查找或创建会话
    4. 加载历史消息 + 附件上下文
    5. 保存用户消息到数据库
    6. 流式生成 AI 回答并实时写入数据库
    7. 记忆开启时自动存储问答对到长期记忆
    """
    data = request.get_json() or {}
    question = data.get("question", "")
    session_id = data.get("session_id")
    attachments = data.get("attachments") or []

    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401

    # 获取功能开关：前端传值优先，否则回退到用户个人配置
    user_cfg = load_config(username)
    enable_thinking = data.get("enable_thinking", user_cfg.get("thinking") == "enabled")
    thinking_strength = data.get("thinking_strength", user_cfg.get("thinking_strength", "high"))
    search = data.get("search", user_cfg.get("search", False))
    memory = data.get("memory", user_cfg.get("memory", False))

    # 查找或创建会话
    if session_id:
        chat_session = ChatSession.query.filter_by(
            id=session_id, username=username
        ).first()
        if not chat_session:
            return jsonify({"error": "session_not_found"}), 404
    else:
        chat_session = ChatSession(username=username, title=generate_title(question))
        db.session.add(chat_session)
        db.session.flush()  # 获取自增 ID
        session_id = chat_session.id

    # 加载会话历史消息
    history = (
        ChatMessage.query.filter_by(session_id=session_id)
        .order_by(ChatMessage.seq.asc())
        .all()
    )
    messages = [{"role": m.role, "content": m.content} for m in history]

    # 附件上下文注入（作为 system 消息追加）
    attachment_context, image_data_list = build_attachment_context(attachments, username, session_id)
    if attachment_context:
        messages = messages + [{"role": "system", "content": attachment_context}]

    # 附件 Markdown 用于消息存储
    attachment_markdown = build_attachment_markdown(attachments, username, session_id)
    question_for_storage = question
    if attachment_markdown:
        question_for_storage = f"{question}\n\n{attachment_markdown}".strip()

    # 首个用户消息时更新会话标题
    if not any(m.role == "user" for m in history):
        chat_session.title = generate_title(question)

    # 保存用户消息（seq 递增）
    next_seq = (history[-1].seq + 1) if history else 1
    db.session.add(
        ChatMessage(session_id=session_id, role="user", content=question_for_storage, seq=next_seq)
    )
    db.session.commit()

    @stream_with_context
    def generate():
        """流式生成器 —— 逐 token 输出并收集完整回答后持久化。"""
        answer_chunks = []
        try:
            for chunk in get_ai_answer_with_messages_stream(
                messages,
                question,
                enable_thinking,
                thinking_strength,
                search,
                memory,
                username=username,
                session_id=session_id,
                image_data_list=image_data_list,
            ):
                answer_chunks.append(chunk)
                yield chunk

            # 完整回答写入数据库
            answer = "".join(answer_chunks)
            db.session.add(
                ChatMessage(
                    session_id=session_id,
                    role="assistant",
                    content=answer,
                    seq=next_seq + 1,
                )
            )
            db.session.add(
                ChatRecord(username=username, question=question_for_storage, answer=answer)
            )
            chat_session.updated_at = datetime.now(timezone.utc)
            db.session.commit()

            # 记忆开启时异步存储问答对到长期记忆
            if memory and answer:
                store_memory(username, question_for_storage, answer,
                             session_id=str(session_id))
        except BaseException:
            db.session.rollback()
            raise

    response = Response(generate(), mimetype="text/plain; charset=utf-8")
    response.headers["X-Session-Id"] = str(session_id)
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"  # 禁用 Nginx 缓冲
    return response


# ============================================================
# 应用初始化
# ============================================================

with app.app_context():
    db.create_all()  # 自动创建缺失的数据库表

# 启动 MCP 管理器（后台线程连接 MCP 服务器）
mcp_mgr = get_mcp_manager()
mcp_mgr.register_server("web_search", "web_search_server.py", "联网搜索服务")
mcp_mgr.start()
print("[MCP] MCP 管理器已启动")

if __name__ == "__main__":
    app.run(debug=True)
