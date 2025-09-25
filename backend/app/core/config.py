from functools import lru_cache
from typing import List, Sequence

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    app_name: str = "Find Your Balance"
    api_v1_prefix: str = "/api/v1"
    secret_key: str = "super-secret-development-key"
    access_token_expire_minutes: int = 60 * 24
    allowed_hosts: Sequence[str] = ("*")

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/fyb"
    redis_url: str = "redis://localhost:6379/0"

    cors_origins: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    class Config:
        env_prefix = "FYB_"


@lru_cache
def get_settings() -> Settings:
    return Settings()
