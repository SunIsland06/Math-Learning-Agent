from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import requests

app = Flask(__name__)
app.secret_key = "123456789"

# =====================数据库表=========================
# MySQL数据库 只需改自己的MySQL密码》》你的MySQL密码
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:你的MySQL密码@127.0.0.1:3306/flask_chat?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 绑定数据库
db = SQLAlchemy(app)

# 用户表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# 聊天记录表
class ChatRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

# ====================SHA256加密工具函数 ====================
def sha256_encrypt(pwd):
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()

# ====================大模型接口函数====================
#在线大模型API 只修改地址和密钥和名称》》你的大模型接口地址 你的密钥 模型名称
def get_ai_answer(question):
    url = "你的大模型接口地址"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 你的密钥"
    }
    payload = {
        "prompt": question,
        "model": "模型名称"
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=30)
        return res.json()["result"]
    except Exception as e:
        return f"大模型请求异常：{str(e)}"
# ==================== 注册路由 ====================
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        # 判断账号是否存在
        if User.query.filter_by(username=username).first():
            return "账号已存在！<a href='/register'>返回注册</a>"
        encrypt_pwd = sha256_encrypt(pwd)
        # 存入MySQL
        new_user = User(username=username, password=encrypt_pwd)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# ==================== 登录路由 ====================
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        user = User.query.filter_by(username=username).first()
        if not user:
            return "账号或密码错误！<a href='/login'>重新登录</a>"
        if sha256_encrypt(pwd) == user.password:
            session['username'] = username
            return redirect(url_for('index'))
        return "账号或密码错误！<a href='/login'>重新登录</a>"
    return render_template('login.html')

# ==================== 退出登录 ====================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ==================== 问答主页 ====================
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    history = ChatRecord.query.filter_by(username=session['username']).all()
    return render_template('index.html', username=session['username'], history=history)

# ====================  问答接口 ====================
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question','')
    # 调用大模型
    answer = get_ai_answer(question)
    username = session.get('username','')
    # 聊天记录存入MySQL
    new_record = ChatRecord(username=username, question=question, answer=answer)
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"answer": answer})

# 程序启动自动创建数据表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
