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

# 将 src 根目录加入模块搜索路径
sys.path.append(str(Path(__file__).resolve().parents[1]))
from model.model import Model
from mcp_services.mcp_manager import get_mcp_manager

app = Flask(__name__)
app.secret_key = "123456789"

# 数据库连接配置
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:672284Aa.@127.0.0.1:3306/flask_chat?charset=utf8mb4"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
USERDATA_ROOT = Path(__file__).resolve().parents[2] / "userdata"

# 新增：是否开启大模型思考过程等设置
ENABLE_AI_THINKING = False 
THINKING_STRENGTH = "high"  # 默认为 high，可选 high / max
ENABLE_SEARCH = False
ENABLE_MEMORY = False

db = SQLAlchemy(app)


class User(db.Model):
    # 用户信息表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class ChatRecord(db.Model):
    # 简易问答记录表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)


class ChatSession(db.Model):
    # 会话表
    __tablename__ = "chat_session"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ChatMessage(db.Model):
    # 会话消息表
    __tablename__ = "chat_message"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    session_id = db.Column(db.BigInteger, nullable=False, index=True)
    role = db.Column(db.Enum("system", "user", "assistant"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    seq = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


def sha256_encrypt(pwd):
    # 密码哈希
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()


def generate_title(question: str) -> str:
    # 根据首句生成会话标题
    text = (question or "").strip()
    if not text:
        return f"new-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}"
    return text[:15]


def sanitize_path_part(value: str) -> str:
    # 过滤路径中的非法字符
    return re.sub(r"[^a-zA-Z0-9._-]", "_", value or "")


def get_user_session_dir(username: str, session_id: str | int, ensure: bool = True) -> Path:
    # 获取用户会话目录
    safe_user = sanitize_path_part(str(username))
    safe_session = sanitize_path_part(str(session_id))
    target = USERDATA_ROOT / safe_user / safe_session
    if ensure:
        target.mkdir(parents=True, exist_ok=True)
    return target


def build_attachment_context(attachments, username: str, session_id: str | int) -> str:
    # 生成供模型使用的附件上下文
    if not attachments:
        return ""

    lines = []
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
            try:
                text = file_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                text = ""
            if len(text) > 4000:
                text = text[:4000] + "\n...[truncated]"
            lines.append(f"[Markdown File] {name}\n```\n{text}\n```")
        elif kind == "image":
            lines.append(f"[Image] {name}\nURL: {url}")
        else:
            lines.append(f"[File] {name}\nURL: {url}")

    if not lines:
        return ""

    return "附件如下：\n" + "\n\n".join(lines)


def build_attachment_markdown(attachments, username: str, session_id: str | int) -> str:
    # 生成供存储的附件 Markdown
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

 # 新增； Model 类内部有一个属性或方法可以控制是否输出思考过程（只是假设方法，需要更多补充）
def get_ai_answer_with_messages_stream(
    messages,
    question,
    enable_thinking=False,
    thinking_strength="high",
    search=False,
    memory=False,
    username="",
    session_id="",
):
    # 组装模型上下文并流式输出回答
    model = Model()
    if username and session_id:
        output_dir = get_user_session_dir(username, session_id, ensure=True)
        model.skill_caller.context = {
            "output_dir": str(output_dir),
            "output_url_prefix": f"/userdata/{sanitize_path_part(username)}/{sanitize_path_part(str(session_id))}/",
        }
    model.messages = model.messages[:1] + messages
    # 假设 Model 类支持设置这些属性(需要补充)
    model.enable_thinking = enable_thinking
    model.thinking_strength = thinking_strength
    model.enable_search = search
    model.enable_memory = memory
    yield from model.stream_chat_chunks(question)


@app.route("/register", methods=["GET", "POST"])
def register():
    # 注册接口
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
    # 登录接口
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
    # 退出登录
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def index():
    # 首页（历史记录）
    if "username" not in session:
        return redirect(url_for("login"))
    history = ChatRecord.query.filter_by(username=session["username"]).all()
    return render_template("index.html", username=session["username"], history=history)


@app.route("/userdata/<username>/<session_id>/<path:filename>")
def userdata_files(username, session_id, filename):
    # 静态附件下载
    safe_user = sanitize_path_part(username)
    safe_session = sanitize_path_part(session_id)
    base_dir = USERDATA_ROOT / safe_user / safe_session
    return send_from_directory(base_dir, filename, as_attachment=False)


@app.route("/session/new", methods=["POST"])
def session_new():
    # 新建会话
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401
    new_session = ChatSession(username=username, title="new")
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"session_id": new_session.id})


@app.route("/session/list", methods=["GET"])
def session_list():
    # 获取会话列表
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
    # 获取指定会话的消息记录
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
    # 更新会话标题
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
    # 删除会话及其消息
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


@app.route("/upload", methods=["POST"])
def upload():
    # 上传附件并保存到用户会话目录
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

    original_name = Path(file.filename).name
    ext = Path(original_name).suffix.lower()
    allowed_ext = {".png", ".jpg", ".jpeg", ".webp", ".md", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".word", ".ppt"}
    if ext not in allowed_ext:
        return jsonify({"error": "unsupported_type"}), 400

    safe_stem = sanitize_path_part(Path(original_name).stem) or "upload"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
    stored_name = f"{safe_stem}-{stamp}{ext}"
    target_dir = get_user_session_dir(username, session_id, ensure=True)
    target_path = target_dir / stored_name
    file.save(target_path)

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

#从前端传来的 JSON 数据里获取这个开关（如果前端没传，则默认使用配置文件中的全局设置），并将其传给工具函数
@app.route("/ask", methods=["POST"])
def ask():
    # 主问答接口，支持附件与流式输出
    data = request.get_json() or {}
    question = data.get("question", "")
    session_id = data.get("session_id")
    attachments = data.get("attachments") or []
    
    # 获取前端传来的开关，如果没有传，则读取 config 中的默认值
    enable_thinking = data.get("enable_thinking", app.config.get("ENABLE_AI_THINKING"))
    thinking_strength = data.get("thinking_strength", app.config.get("THINKING_STRENGTH"))
    search = data.get("search", app.config.get("ENABLE_SEARCH"))
    memory = data.get("memory", app.config.get("ENABLE_MEMORY"))
    
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401

    if session_id:
        chat_session = ChatSession.query.filter_by(
            id=session_id, username=username
        ).first()
        if not chat_session:
            return jsonify({"error": "session_not_found"}), 404
    else:
        chat_session = ChatSession(username=username, title=generate_title(question))
        db.session.add(chat_session)
        db.session.flush()
        session_id = chat_session.id

    history = (
        ChatMessage.query.filter_by(session_id=session_id)
        .order_by(ChatMessage.seq.asc())
        .all()
    )
    messages = [{"role": m.role, "content": m.content} for m in history]

    attachment_context = build_attachment_context(attachments, username, session_id)
    if attachment_context:
        messages = messages + [{"role": "system", "content": attachment_context}]

    attachment_markdown = build_attachment_markdown(attachments, username, session_id)
    question_for_storage = question
    if attachment_markdown:
        question_for_storage = f"{question}\n\n{attachment_markdown}".strip()

    if not any(m.role == "user" for m in history):
        chat_session.title = generate_title(question)

    next_seq = (history[-1].seq + 1) if history else 1
    db.session.add(
        ChatMessage(session_id=session_id, role="user", content=question_for_storage, seq=next_seq)
    )
    db.session.commit()

    @stream_with_context
    def generate():
        # 流式生成并写入数据库
        answer_chunks = []
        try:
            # 将开关传递给流式生成函数
            for chunk in get_ai_answer_with_messages_stream(
                messages,
                question,
                enable_thinking,
                thinking_strength,
                search,
                memory,
                username=username,
                session_id=session_id,
            ):
                answer_chunks.append(chunk)
                yield chunk

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
        except BaseException:
            db.session.rollback()
            raise

    response = Response(generate(), mimetype="text/plain; charset=utf-8")
    response.headers["X-Session-Id"] = str(session_id)
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


with app.app_context():
    db.create_all()

# ---- 启动 MCP 管理器 ----
mcp_mgr = get_mcp_manager()
mcp_mgr.register_server("web_search", "web_search_server.py", "联网搜索服务")
mcp_mgr.start()
print("[MCP] MCP 管理器已启动")

if __name__ == "__main__":
    app.run(debug=True)
