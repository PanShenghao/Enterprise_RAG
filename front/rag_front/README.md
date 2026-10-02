# rag_front

RAG Agent 系统的前端管理工作台（Vue 3 + Vite + TypeScript + Element Plus + Pinia）。

## 页面模块

- 总览看板（DashboardView）
- 上传入库（IngestView）
- 文档管理（DocumentsView）
- Chunk 管理（ChunksView）
- 检索调试（RetrievalView）
- Agent 对话（ChatView）

## 开发

```sh
npm install
npm run dev
```

本地开发已配置代理：`/api/v1`、`/health` 转发到 `http://127.0.0.1:8000`。

@author: psh
