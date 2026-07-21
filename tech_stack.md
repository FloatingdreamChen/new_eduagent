# 技术栈概览

简要列出本仓库核心使用的语言、框架、库和工具，便于快速了解项目依赖与运行方式。

## 概览
- 主语言：Python 3.11.x（项目检测到环境为 3.11.15）
- 前端：TypeScript + Vue 3（Vite 打包）
- 架构：FastAPI 后端 + Vite + Vue 前端

## 后端（Python）
- Web 框架：FastAPI
- ASGI 服务器：uvicorn
- 配置 / settings：pydantic / pydantic-settings
- 异步 HTTP：httpx
- 文件上传：python-multipart
- SSE：sse-starlette

## 前端
- 构建工具：Vite
- 框架：Vue 3
- 状态管理：Pinia
- 路由：vue-router
- UI：Element Plus
- HTTP：axios
- 代码高亮：highlight.js
- Markdown 渲染：markdown-it

## 模型与机器学习
- LangChain / LangGraph（pipeline 与结构化使用）
- Transformers / sentence-transformers / torch（本地模型推理、意图分类、精排）
- FlagEmbedding / BGE-M3（本地嵌入）
- BGE-Reranker（重排序）

## 向量与数据库
- 向量库：Milvus（客户端：pymilvus）
- 关系型：PostgreSQL（异步驱动 asyncpg + SQLAlchemy asyncio）
- 数值库：numpy

## 文档与解析
- Word：python-docx
- PDF：pymupdf（import 名为 fitz）

## 认证与安全
- JWT：python-jose
- 密码哈希：passlib[bcrypt]（兼容 bcrypt==4.x）

## 工具与协议
- MCP：mcp Python SDK（项目中有 MCP 子应用实现，用于知识库与网络搜索）
- Web 搜索：duckduckgo-search
- 环境/配置：python-dotenv（.env.local）

## 测试与开发
- 测试：pytest、pytest-asyncio
- 类型检查 / 编译（前端）：TypeScript、vue-tsc

## 部署与脚本
- 项目包含 `docker-compose.yml`（项目根）用于容器化编排（若配置）
- 常用脚本位于 `scripts/`（如构建知识库、初始化 DB 等）

## 运行（本地开发）示例
- 启动后端（本地调试）：

  python -m backend.main

- 或使用 uvicorn：

  uvicorn backend.main:app --host 0.0.0.0 --port 8000

- 启动前端（进入 frontend）：

  npm install
  npm run dev

前端默认通过 Vite 运行（vite 配置中 proxy 到 `http://localhost:8000`，见 `frontend/vite.config.ts`）。

## 关键文件参考
- Python 依赖：[requirements.txt](requirements.txt)
- 前端依赖与脚本：[frontend/package.json](frontend/package.json)
- 前端配置：[frontend/vite.config.ts](frontend/vite.config.ts)
- 后端入口：[backend/main.py](backend/main.py#L1-L200)

---

