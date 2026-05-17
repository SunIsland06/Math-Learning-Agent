# Math-Learning-Agent — 数智教师

**一个面向大学工科数学的 AI 智能教学系统**

体验网址：**[http://agent.sun-island.cn/](http://agent.sun-island.cn/)**

数智教师不再只是"你问我答"的通用大模型，而是一位能**记住你的学习情况、严格遵循指定教材、引导式教学、自动生成学习报告和测验的智能导师**。通过 **LLM 大模型 + RAG 知识库 + 工具调用 + 长期记忆**，把语言模型变成"教、练、测、评"一体化的教学闭环系统。

---

## 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| **LLM** | DeepSeek v4 Pro | 主力推理模型，支持多模态（文本+图片） |
| **Web 框架** | Flask + Jinja2 | 后端服务和模板渲染 |
| **数据库** | MySQL + SQLAlchemy | 用户数据、会话消息持久化 |
| **向量数据库** | ChromaDB | 教材知识库和长期记忆的向量存储 |
| **嵌入模型** | Ollama nomic-embed-text | 文本向量化（768维） |
| **符号计算** | SymPy | 导数、积分、极限、方程求解等 |
| **数值计算** | NumPy + Matplotlib | 数值运算和可视化 |
| **MCP 协议** | Model Context Protocol | 工具服务器标准化通信 |
| **文档处理** | pdfplumber + python-docx | PDF/Word 文档解析 |
| **PDF 生成** | fpdf2 | 学习报告、试卷 PDF 导出 |
| **搜索引擎** | DuckDuckGo (DDGS) | 联网搜索 |

**本项目开发过程中使用过的 LLM**：DeepSeek v4 Pro、Codex 5.2、Codex 5.3、ChatGPT 5.5

---

## 功能亮点

### 1. 多模态数学问题输入
- 支持上传**图片**（手写/印刷题目）、**PDF 教材**、**Word 文档**、**Markdown 文件**
- 图片自动通过视觉模型识别数学题目和公式
- PDF/Word 自动提取文本内容注入对话上下文

### 2. 教材级 RAG 检索增强
- 基于用户上传的教材构建向量知识库
- 回答可附带原文出处、学科分类和章节定位
- 混合检索策略：向量相似度(60%) + 词汇匹配(40%) × 学科加权
- RAG 功能支持一键开关

### 3. 智能引导式教学
- **推导型问题**：不直接给答案，分步引导、反问验证
- **知识型问题**：清晰准确回答，主动拓展关联知识
- **模糊型问题**：温和追问，帮助学生明确需求
- 不完整条件的问题主动发起澄清提问

### 4. 丰富的数学工具生态（11 个技能）

| 技能 | 功能 |
|------|------|
| `symbolic_computation` | 符号计算：求导、积分、极限、方程求解、矩阵运算、级数展开 |
| `geometry` | 几何图形：2D 函数曲线、3D 曲面图、文本卡片 |
| `graph_plotting` | 函数图像：多函数对比、参数方程、极坐标图 |
| `step_by_step_solver` | 分步解题：自动生成逐步推理过程 |
| `code_execution` | 代码执行：安全沙箱运行 Python 数值计算 |
| `latex_render` | 公式渲染：LaTeX 公式转高清 PNG 图片 |
| `wolfram_alpha` | Wolfram Alpha：复杂数学计算和公式推导 |
| `quiz_system` | 测验系统：阶梯出题、自动批改、相似题推荐 |
| `study_plan` | 学习计划：个性化学习/复习/备考计划生成 |
| `document_generation` | 文档生成：学习报告导出为 PDF/Word/Markdown |
| `web_search` | 联网搜索：获取最新资料，查证定理公式 |

### 5. 个性化学习闭环
- **长期记忆**：永久保存用户画像、知识薄弱点、错题本
- **自适应出题**：根据能力动态调整题目难度
- **相似题推荐**：针对错题自动推荐巩固练习
- **测验系统**：出题 → 作答 → 批改 → 推荐的四步闭环

### 6. 多格式报告输出
- 对话内容支持 Markdown 实时渲染 + KaTeX 数学公式
- 一键生成学习报告/试卷并导出为 **PDF、Word 或 Markdown** 下载
- 支持自定义页眉页脚、目录等

---

## 与通用大模型的差异化优势

| 对比维度 | 通用大模型网页版 | 本项目的数智教师 |
|-----------|------------------|-------------------|
| **长期记忆** | 仅当前会话有效 | 学生画像、薄弱点、错题本永久保存 |
| **教材锁定** | 无法限定知识源 | 基于教材构建向量库，回答附带出处 |
| **教学策略** | 直接给答案 | 分步引导、反问检查、主动追问 |
| **学习闭环** | 仅问答 | 微课讲解 → 阶梯出题 → 批改 → 学习报告 |
| **多模态输入** | 通常仅图片 | 图片/PDF/Word/Markdown 全支持 |
| **数学工具** | 无专用工具 | 11 个专业技能，覆盖符号计算到文档生成 |
| **个性化** | 千人一面 | 动态抽题、相似题推荐、薄弱点精准攻克 |
| **文档导出** | 不支持 | PDF/Word/Markdown 一键生成下载 |

---

## 快速部署

### 前置要求
- Python 3.10+
- MySQL 8.0+
- Ollama（用于向量嵌入）
- Conda（推荐，用于环境管理）

### 1. 克隆项目
```bash
git clone <your-repo-url>
cd Math-Learning-Agent
```

### 2. 环境配置

**方式一：Conda 导入（推荐）**
```bash
conda env create -f environment.yml
conda activate Math-Learning-Agent
```

**方式二：Pip 安装**
```bash
pip install -r requirements.txt
```

### 3. MySQL 配置
1. 安装并启动 MySQL 服务
2. 创建数据库：
```sql
CREATE DATABASE flask_chat DEFAULT CHARACTER SET utf8mb4;
```
3. 修改 `src/web/app.py` 第 32 行的数据库连接字符串：
```python
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:你的密码@127.0.0.1:3306/flask_chat?charset=utf8mb4"
)
```

### 4. API 配置
编辑 `config/global.yml`：
```yaml
APIUrl: https://api.deepseek.com/chat/completions
key: 你的DeepSeek-API-Key
model: deepseek-v4-pro
wolfram_app_id:    # Wolfram Alpha App ID（可选）
```

### 5. Ollama 配置
```bash
# 安装 Ollama 后拉取嵌入模型
ollama pull nomic-embed-text
```

### 6. 构建知识库（可选）
```bash
# 将教材 .md 文件放入 src/rag/textbook/，然后依次运行
python src/rag/chunking.py      # 1. 分块
python src/rag/embedding.py     # 2. 向量化
python src/rag/database.py      # 3. 入库
```

### 7. 启动应用
```bash
python src/web/app.py
```
访问 **http://127.0.0.1:5000** 注册并登录即可使用。

---

## 项目架构

```
Math-Learning-Agent/
├── config/global.yml          # 全局配置（API密钥、模型选择）
├── src/
│   ├── web/app.py             # Flask Web 应用入口
│   ├── model/model.py         # LLM 模型封装（DeepSeek API）
│   ├── skill/
│   │   ├── skillManager.py    # 技能自动发现与管理
│   │   └── skillCall.py       # 技能调用执行引擎
│   ├── rag/                   # RAG 检索增强管道
│   │   ├── chunking.py        # 教材分块
│   │   ├── embedding.py       # 向量化
│   │   ├── database.py        # ChromaDB 入库
│   │   └── integration.py     # 混合检索（向量+词汇+学科加权）
│   ├── memory/memory_manager.py # 长期记忆管理
│   ├── mcp_services/          # MCP 协议服务
│   │   ├── mcp_manager.py     # MCP 客户端管理器
│   │   └── web_search_server.py # 联网搜索 MCP 服务
│   ├── config/globalConfig.py # 全局配置单例
│   ├── utils/
│   │   ├── user_config.py     # 用户个人配置管理
│   │   └── document_parser.py # 文档解析（PDF/Word/图片）
│   └── prompt/system.md       # 系统提示词
├── skill/                     # 技能实现目录（11个技能）
│   ├── symbolic_computation/  # 符号计算
│   ├── geometry/              # 几何图形
│   ├── graph_plotting/        # 函数图像
│   ├── step_by_step_solver/   # 分步解题
│   ├── code_execution/        # 安全代码执行
│   ├── latex_render/          # LaTeX 公式渲染
│   ├── wolfram_alpha/         # Wolfram Alpha 查询
│   ├── quiz_system/           # 测验系统
│   ├── study_plan/            # 学习计划生成
│   ├── document_generation/   # 文档生成（PDF/Word）
│   └── math-guided-teaching/  # 引导式教学策略
└── requirements.txt           # Python 依赖
```

---

## 使用示例

### 示例 1：上传图片题目求解
1. 在对话界面点击上传按钮，选择手写数学题的图片
2. 输入："请帮我看看这道题怎么做"
3. 数智教师识别图片中的题目，判断为推导型，开始分步引导

### 示例 2：生成学习报告
1. 完成一段时间的学习后，输入："帮我生成这周的学习报告"
2. 数智教师回顾对话历史、分析薄弱点
3. 调用 `document_generation` 技能生成 PDF 报告，一键下载

### 示例 3：自适应测验
1. 输入："给我出几道导数的练习题"
2. 系统调用 `quiz_system` 生成阶梯式题目
3. 学生作答后，系统自动批改
4. 针对错题推荐相似题目巩固

### 示例 4：Wolfram Alpha 计算
1. 在 config/global.yml 配置 Wolfram Alpha App ID
2. 输入："用 Wolfram Alpha 计算 ∫x·sin(x)dx"
3. 系统返回详细计算步骤和可视化图表

---

## 未来规划

- [ ] **语音输入**：支持语音提问和语音讲解
- [ ] **手写识别增强**：集成专业数学 OCR 引擎（如 LaTeX-OCR）
- [ ] **多教材对比**：同时检索多本教材，进行知识点交叉验证
- [ ] **学习仪表盘**：可视化展示学习进度、知识点掌握热力图
- [ ] **协作学习**：支持学习小组和同伴互评
- [ ] **移动端适配**：PWA 支持，随时随地学习
- [ ] **更多 LLM 接入**：支持 OpenAI、Claude 等多模型切换

---

## License

MIT License
