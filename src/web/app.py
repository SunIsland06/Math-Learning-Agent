from datetime import datetime
import hashlib
import sys
from pathlib import Path

from flask import (
    Flask,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    stream_with_context,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy

sys.path.append(str(Path(__file__).resolve().parents[1]))
from model.model import Model

app = Flask(__name__)
app.secret_key = "123456789"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:672284Aa.@127.0.0.1:3306/flask_chat?charset=utf8mb4"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 新增：是否开启大模型思考过程等设置
    ENABLE_AI_THINKING = False 
    THINKING_STRENGTH = "high"  # 默认为 high，可选 high / max
    ENABLE_SEARCH = False
    ENABLE_MEMORY = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class ChatRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)


class ChatSession(db.Model):
    __tablename__ = "chat_session"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ChatMessage(db.Model):
    __tablename__ = "chat_message"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    session_id = db.Column(db.BigInteger, nullable=False, index=True)
    role = db.Column(db.Enum("system", "user", "assistant"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    seq = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


def sha256_encrypt(pwd):
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()


def generate_title(question: str) -> str:
    text = (question or "").strip()
    if not text:
        return f"new-{datetime.utcnow().strftime('%Y%m%d-%H%M')}"
    return text[:15]

 # 新增； Model 类内部有一个属性或方法可以控制是否输出思考过程（只是假设方法，需要更多补充）
def get_ai_answer_with_messages_stream(messages, question, enable_thinking=False,thinking_strength="high", search=False, memory=False):
    model = Model()
    model.messages = model.messages[:1] + messages
    # 假设 Model 类支持设置这些属性(需要补充)
    model.enable_thinking = enable_thinking
    model.thinking_strength = thinking_strength
    model.enable_search = search
    model.enable_memory = memory
    yield from model.stream_chat_chunks(question)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        if User.query.filter_by(username=username).first():
            return "账号已存在！<a href='/register'>返回注册</a>"
        encrypt_pwd = sha256_encrypt(pwd)
        db.session.add(User(username=username, password=encrypt_pwd))
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
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
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    history = ChatRecord.query.filter_by(username=session["username"]).all()
    return render_template("index.html", username=session["username"], history=history)


@app.route("/session/new", methods=["POST"])
def session_new():
    username = session.get("username", "")
    if not username:
        return jsonify({"error": "not_login"}), 401
    new_session = ChatSession(username=username, title="new")
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"session_id": new_session.id})


@app.route("/session/list", methods=["GET"])
def session_list():
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

#从前端传来的 JSON 数据里获取这个开关（如果前端没传，则默认使用配置文件中的全局设置），并将其传给工具函数
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    question = data.get("question", "")
    session_id = data.get("session_id")
    
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

    if not any(m.role == "user" for m in history):
        chat_session.title = generate_title(question)

    next_seq = (history[-1].seq + 1) if history else 1
    db.session.add(
        ChatMessage(session_id=session_id, role="user", content=question, seq=next_seq)
    )

    @stream_with_context
    def generate():
        answer_chunks = []
        try:
            # 将开关传递给流式生成函数
            for chunk in get_ai_answer_with_messages_stream(messages, question,enable_thinking, thinking_strength, search, memory): 
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
            chat_session.updated_at = datetime.utcnow()
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


if __name__ == "__main__":
    app.run(debug=True)
