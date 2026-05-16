# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Math-Learning-Agent is an AI-powered math tutor web app built with Flask. It uses an LLM (DeepSeek API) with RAG (ChromaDB + Ollama embeddings), a dynamic skill/tool-calling system, and MySQL-backed session persistence to create a guided teaching loop: lecture → quiz → grading → report.

## Running the app

```bash
# Start the Flask dev server
python src/web/app.py

# The RAG pipeline has three stages (run in order):
python src/rag/chunking.py          # 1. Chunk textbook .md files → chunks_result.json
python src/rag/embedding.py         # 2. Vectorize chunks via Ollama → vectorized_chunks.json
python src/rag/database.py          # 3. Insert vectors into ChromaDB

# Individual skill test
python skill/geometry/geometry.py
```

The web app runs on Flask's default port (5000) in debug mode. External dependencies required:
- **MySQL** on `127.0.0.1:3306` (database `flask_chat`, credentials in `app.py` line 30)
- **Ollama** on `127.0.0.1:11434` with model `nomic-embed-text` pulled
- **DeepSeek API** endpoint configured in `config/global.yml`

## Architecture

```
Frontend (Jinja2 + vanilla JS)
    │  SSE streaming
    ▼
Flask app (src/web/app.py)
    │  calls
    ▼
Model (src/model/model.py) ── RAG retrieval (src/rag/integration.py)
    │                              │
    │  tool calls                  ├── chunking.py (markdown → chunks)
    ▼                              ├── embedding.py (chunks → vectors via Ollama)
SkillCaller (src/skill/skillCall.py)    └── database.py (vectors → ChromaDB)
    │
    ▼
SkillManager (src/skill/skillManager.py)
    │  auto-discovers
    ▼
skill/<name>/SKILL.md  +  skill/<name>/*.py
```

### Skill system (key design)

Skills are auto-discovered from `skill/` directory. Each skill is a subfolder containing:
- `SKILL.md` — YAML frontmatter (`name`, `description`) + Markdown body with usage instructions
- Python entry file(s) referenced in the body via `调用: xxx.py`

The SkillManager scans all subfolders on startup, parses frontmatter, and builds OpenAI-compatible tool definitions. When the LLM issues a tool call, SkillCaller dynamically loads the Python module and calls `skill_entry(payload)`, `run(payload)`, `main(payload)`, or `handle(payload)`.

To add a new skill: create `skill/<name>/SKILL.md` with frontmatter, optionally add a Python entry file, restart the app. No registration needed.

### RAG pipeline

Textbooks are stored as Markdown in `src/rag/textbook/`. The pipeline:
1. `chunking.py` splits by markdown headings with paragraph-aware boundaries (~1000 char chunks, 120 char overlap)
2. `embedding.py` calls Ollama (`nomic-embed-text`) to vectorize each chunk
3. `database.py` inserts vectors into ChromaDB (`src/rag/db/math_knowledge_db/`)
4. At query time, `integration.py` retrieves top-k chunks with hybrid scoring (cosine distance + lexical term matching), and `Model._build_rag_message()` injects them as a system message

### Key data flow (chat)

1. User sends message via web UI → `POST /ask`
2. `app.py` loads session history, appends user message to DB
3. `get_ai_answer_with_messages_stream()` creates a Model instance, sets its context (output_dir for image generation), and streams chunks
4. `Model.stream_chat_chunks()` sends the conversation + tools to DeepSeek API
5. If the LLM returns tool calls, they're executed by SkillCaller and results fed back for a follow-up completion
6. The full answer is persisted to `ChatMessage` and `ChatRecord` tables

### Config

`config/global.yml` — loaded by singleton `GlobalConfig` in `src/config/globalConfig.py`. Contains API URL, key, model name, thinking/search/memory defaults.

## Key conventions

- The system prompt is in `src/prompt/system.md` — it defines the teaching persona and the decision tree (推导型 → call `math-guided-teaching` skill, 知识型 → answer directly, 模糊型 → clarify)
- `sys.path` hacks: several files append the repo root or `src/` to `sys.path` for cross-package imports. Keep imports relative to the file's location when adding new modules.
- Session-scoped file storage: uploaded attachments go to `userdata/<username>/<session_id>/`, served via `/userdata/...` routes
- Markdown rendering: frontend uses markdown-it + KaTeX for math. Use `$$` for display math, `$` for inline. The normalizeMathDelimiters function converts `\[...\]` / `\(...\)` syntax.
