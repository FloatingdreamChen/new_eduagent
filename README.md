# EduAgent

EduAgent 是一个面向教学场景的 AI 助教系统，提供智能问答、试卷批改、简历审查、模拟面试和统一多 Agent 对话入口。项目采用前后端分离架构，后端基于 FastAPI、LangGraph、LangChain 和本地 BGE 系列模型，前端基于 Vue 3、Vite、Pinia 和 Element Plus。

## 功能模块

- 智能问答：基于知识库检索、BGE-M3 向量召回和 Reranker 精排生成回答。
- 统一聊天：根据用户意图路由到 QA、试卷、简历、面试等 Agent。
- 试卷批改：支持学生提交答案，AI 进行评分、反馈和薄弱点分析。
- 简历审查：上传简历后生成多维度评估报告和修改建议。
- 模拟面试：围绕岗位、简历和技术栈进行多轮面试对话。
- MCP 服务：暴露知识库和 Web Search MCP 子应用，便于工具化调用。

## 技术栈

### 后端

- Python 3.11
- FastAPI / Uvicorn
- LangChain / LangGraph
- PostgreSQL / SQLAlchemy / asyncpg
- Milvus / pymilvus
- BGE-M3 / BGE-Reranker / sentence-transformers
- MCP Python SDK

### 前端

- Vue 3
- Vite
- TypeScript
- Pinia
- Vue Router
- Element Plus
- Markdown-it / highlight.js

### 基础设施

- Docker Compose
- PostgreSQL 15
- Milvus standalone
- etcd
- MinIO

## 目录结构

```text
.
├── backend/                 # FastAPI 后端服务
│   ├── agents/              # QA、试卷、简历、面试 Agent
│   ├── api/                 # API 路由
│   ├── core/                # LLM、知识库、重排、记忆、编排等核心能力
│   ├── db/                  # 数据库迁移
│   ├── mcp/                 # MCP 服务
│   └── models/              # 本地模型目录（不提交 Git）
├── frontend/                # Vue 3 前端
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── scripts/                 # 初始化、建库、种子数据和手工测试脚本
├── docker-compose.yml       # 本地 PostgreSQL / Milvus 环境
├── requirements.txt         # 后端 Python 依赖
└── README.md
```

## 本地启动

### 1. 准备环境变量

项目使用根目录 `.env.local` 读取本地配置。该文件包含数据库密码、JWT 密钥、模型服务密钥等敏感信息，不应提交到 Git。

需要的常见变量包括：

```env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=eduagent
DB_USER=eduagent_user
DB_PASSWORD=your_password

MILVUS_HOST=localhost
MILVUS_PORT=19531

JWT_SECRET_KEY=your_jwt_secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=10080

DEEPSEEK_API_KEY=your_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEEPSEEK_MODEL_CHAT=deepseek-chat
DEEPSEEK_MODEL_CODER=deepseek-coder
```

### 2. 启动基础设施

```bash
cd /Users/chenshuaiwen/new_eduagent
docker-compose --env-file .env.local up -d
```

服务端口：

- PostgreSQL: `localhost:5433`
- Milvus: `localhost:19531`

### 3. 启动后端

```bash
cd /Users/chenshuaiwen/new_eduagent
source .venv/bin/activate
python -m backend.main
```

启动成功后会看到：

```text
Uvicorn running on http://0.0.0.0:8000
```

健康检查：

```bash
curl http://127.0.0.1:8000/health
```

### 4. 启动前端

```bash
cd /Users/chenshuaiwen/new_eduagent/frontend
npm install
npm run dev
```

默认访问地址：

```text
http://localhost:3000
```

## 常用脚本

```bash
# 检查环境配置
python scripts/check_env.py

# 初始化 Milvus Collection
python scripts/init_milvus.py

# 构建知识库
python scripts/build_knowledge_base.py

# 初始化示例数据
python scripts/seed_data.py

# 初始化标准试卷数据
python scripts/seed_standard_exam.py
```

## 开发说明

- `.venv/` 是本地 Python 虚拟环境，不提交 Git。
- `.uv-cache/` 是 uv 的本地缓存目录，不是运行环境，不提交 Git。
- `frontend/node_modules/` 是前端依赖目录，不提交 Git。
- `backend/models/` 存放本地模型权重，体积较大，不提交 Git。
- `.env.local` 包含敏感配置，不提交 Git。

## API 文档

后端启动后可访问：

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Git 提交前检查

建议提交前确认忽略文件生效：

```bash
git status --short
```

不应提交以下内容：

- `.env.local`
- `.venv/`
- `.uv-cache/`
- `frontend/node_modules/`
- `backend/models/`
- `*.db`
- `frontend.zip`
