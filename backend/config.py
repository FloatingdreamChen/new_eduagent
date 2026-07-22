# backend/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
import os

backend_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(backend_dir)
env_files = tuple(
    path
    for path in (
        os.path.join(backend_dir, ".env.local"),
        os.path.join(project_root, ".env.local"),
    )
    if os.path.exists(path)
)


class Settings(BaseSettings):
    # ── 数据库（PostgreSQL）──
    db_host: str = "localhost"
    db_port: int = 5433          # 本机已有 PG:5432，EduAgent 隔离到 5433
    db_name: str = "eduagent"
    db_user: str = ""
    db_password: str = ""

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    # ── Milvus ──
    milvus_host: str = "localhost"
    milvus_port: int = 19531     # 本机已有 Milvus:19530，EduAgent 隔离到 19531

    # ── 大模型 ──
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com/v1"
    deepseek_model_chat: str = "deepseek-chat"
    deepseek_model_coder: str = "deepseek-coder"

    # ── 本地模型路径 ──
    reranker_model_path: str = "./models/reranker/bge-reranker-large"
    classifier_model_path: str = "./models/classifier/all-MiniLM-L6-v2"
    finetuned_classifier_path: str= "./models/classifier/query-classifier-finetuned"  # 与训练时 output_dir 保持一致
    bge_m3_model_path: str = "./models/embedding/bge-m3"

    # ── JWT ──
    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 10080

    # ── MCP Servers ──
    kb_mcp_server_url:  str = "http://localhost:8000/mcp/kb"
    web_search_mcp_url: str = "http://localhost:8000/mcp/web-search"

    # ── Web Search（Tavily 可选，留空则自动切换 DuckDuckGo）──
    tavily_api_key: str = ""

    # ── 应用 ──
    app_env: str = "local"
    app_debug: bool = False
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"
    default_tenant_id: str = "tenant_default"
    class Config:
        env_file = env_files or None
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
if __name__ == '__main__':
    s = get_settings()
    print("jwt_secret_key:", s.jwt_secret_key)
    # print("db_port:", s.db_port)
    print("database_url:", s.database_url)
    # print("default_tenant_id:", s.default_tenant_id)
    # print("两次 get_settings 是同一对象(lru_cache):", get_settings() is get_settings())
