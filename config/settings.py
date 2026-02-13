# finsight/config/settings.py

from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import Optional


class Settings(BaseSettings):
    # ------------------------------------------------------------------
    # Environment
    # ------------------------------------------------------------------

    ENV: str = "development"

    # ------------------------------------------------------------------
    # API Keys - Data Providers
    # ------------------------------------------------------------------

    FMP_API_KEY: Optional[str] = None
    ALPHA_VANTAGE_API_KEY: Optional[str] = None
    POLYGON_API_KEY: Optional[str] = None
    YAHOO_API_KEY: Optional[str] = None

    # ------------------------------------------------------------------
    # Platform
    # ------------------------------------------------------------------

    PLATFORM_API_KEY: Optional[str] = None
    ALLOWED_ORIGINS: Optional[str] = None

    # ------------------------------------------------------------------
    # Rate limiting
    # ------------------------------------------------------------------

    RATE_LIMIT_PUBLIC: str = "30/minute"
    RATE_LIMIT_HEAVY: str = "5/minute"

    # ------------------------------------------------------------------
    # VALIDACIONES AUTOMÁTICAS EN PRODUCCIÓN
    # ------------------------------------------------------------------

    @field_validator("PLATFORM_API_KEY")
    @classmethod
    def validate_platform_key(cls, v, info):
        if info.data.get("ENV") == "production" and not v:
            raise ValueError("PLATFORM_API_KEY es obligatoria en producción")
        return v

    @field_validator("ALLOWED_ORIGINS")
    @classmethod
    def validate_allowed_origins(cls, v, info):
        if info.data.get("ENV") == "production" and not v:
            raise ValueError("ALLOWED_ORIGINS es obligatorio en producción")
        return v

    class Config:
        env_file = ".env"


settings = Settings()

