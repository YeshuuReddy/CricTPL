from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """
    Centralized application configuration.
    Loads environment variables from dev.env files or system environment.
    """

    # ==========================
    # Application Config
    # ==========================
    APP_NAME: str = Field(default="Cric_TPL", description="Application name")
    APP_ENV: str = Field(default="development", description="App environment: development/staging/production")
    DEBUG: bool = Field(default=True, description="Enable/disable debug mode")

    # ==========================
    # Database Config
    # ==========================
    DATABASE_URL: str = Field(
        default="postgresql+psycopg2://postgres:1234@localhost:5432/cric_tpl",
        description="Database connection URL (SQLAlchemy compatible)"
    )

    # ==========================
    # Logging Config
    # ==========================
    LOG_LEVEL: str = Field(default="INFO", description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")

    # ==========================
    # Pydantic Settings Config
    # ==========================
    model_config = SettingsConfigDict(
        env_file="dev.env",  # defaults to dev.env, can override in prod
        env_file_encoding="utf-8",
        case_sensitive=True
    )


# Global settings instance
settings = Settings()

