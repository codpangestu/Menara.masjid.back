from pydantic_settings import BaseSettings
from typing import Optional


class Environment(BaseSettings):
    # Database
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_DATABASE: str = "menara_masjid_revamp"
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = "cauburuk123"

    # JWT
    SECRET_KEY: str = "menara-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # API
    API_KEY: str = "menara23apikey"
    APP_NAME: str = "MENARA API"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = True

    # CORS: origin frontend tambahan (comma separated, opsional)
    CORS_ORIGINS: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env = Environment()
