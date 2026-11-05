# 更新日志

## 2026-11-05

### 修复

- **文档入库时 Milvus 元数据 schema 不一致，导致 PDF 上传失败**
  - 现象：纯文本入库正常，但上传 PDF 时 Milvus 报 `unrecognized dtype` / `Insert missed an field` 错误。
  - 根因：写入 Milvus 的元数据随解析器而异（markdown 有 `section_title` 无 `page_number`，PDF 恰好相反），且误把 PostgreSQL 主数据才有的 `knowledge_base / chunk_index / section_index` 一并写入，导致首次建集合后 schema 固定、后续插入不匹配。
  - 修复：按 README「8.3 当前知识库集合中的字段形态」定义的固定 10 字段收敛元数据，文本字段统一 `str`（缺省 `''`），`page_number` 统一 `int`（缺省 `0`）。涉及文件 `backend/app/rag/ingest.py`。
