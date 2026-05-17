---
name: document_generation
description: 将 Markdown 内容生成为 PDF、Word 或 Markdown 文档，支持自定义页眉页脚、目录、标题样式等。适用于生成学习报告、试卷、学习计划等可下载文档。
---

## 使用说明
当用户需要将学习内容导出为文档时调用此技能。

## 参数
- **input**: 待转换的 Markdown 文本内容（支持 LaTeX 公式、表格、图片链接）
- **params**:
  - `format`: 输出格式 —— "pdf"（默认）/ "docx" / "md"
  - `title`: 文档标题
  - `author`: 作者名（可选）
  - `header_text`: 页眉文字（可选）
  - `footer_text`: 页脚文字（可选）
  - `include_toc`: 是否包含目录（默认 true）
  - `output_dir`: 输出目录路径
  - `output_url_prefix`: URL 前缀

调用: generator.py
