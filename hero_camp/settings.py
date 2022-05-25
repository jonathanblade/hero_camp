from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = Field(default="hero_camp", env="APP_NAME")
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    app_host: str = Field(default="0.0.0.0", env="APP_HOST")
    app_post: int = Field(default=3000, env="APP_PORT")

    api_prefix: str = Field(default="/api", env="API_PREFIX")
    docs_url: Optional[str] = Field(default="/docs", env="DOCS_URL")

    debug_mode: bool = Field(default=False, env="DEBUG_MODE")

    db_host: str = Field(default="postgres", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_user: str = Field(default="root", env="DB_USER")
    db_password: str = Field(default="root", env="DB_PASSWORD")
    db_name: str = Field(default="hero_camp", env="DB_NAME")

    jwt_secret_key: str = Field(default="secret", env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", env="JWT_ALGORITHM")
    jwt_lifetime_in_minutes: int = Field(default=60, env="JWT_LIFETIME_IN_MINUTES")

    superuser_username: str = Field(default="root", env="SUPERUSER_USERNAME")
    superuser_password: str = Field(default="root", env="SUPERUSER_PASSWORD")

    response_timeout_in_seconds: int = Field(
        default=15, env="RESPONSE_TIMEOUT_IN_SECONDS"
    )

    @property
    def db_url(cls) -> str:
        return f"postgresql+asyncpg://{cls.db_user}:{cls.db_password}@{cls.db_host}:{cls.db_port}/{cls.db_name}"


SETTINGS = Settings()
