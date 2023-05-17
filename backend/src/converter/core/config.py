from typing import List
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    MONGODB_DB_NAME: str = "converter"
    APPLICATION_NAME: str = "video-to-audio"

    # ------------ FileUpload Constants -------------#
    FILE_UPLOAD_PATH: str = "./temp"
    FILE_MAX_SIZE: int = 1024 * 1024 * 1024 * 4 #4GB
    FILE_REQUEST_BODY_MAX_SIZE: int = FILE_MAX_SIZE + 1024


    # ------------ AUTH Server URLS ----------#
    AUTHSERVER_TOKEN_VERIFICATION_URL: AnyUrl = AnyUrl("http://localhost:8000/api/v1/auth/verify-tokens", scheme="http")

    # ------------ Connection URI -------------#
    POSTGRES_CONN_URI: AnyUrl
    MONGODB_CONN_URI: AnyUrl

    # ------------ CORS settings --------------#
    CORS_ALLOWED_ORIGINS: List[AnyUrl] = [
        AnyUrl(url="http://localhost:5500", scheme="http"),
        AnyUrl(url="https://abhinasregmi.com.np", scheme="https"),
    ]

    
@lru_cache(maxsize=128)
def _settings():
    return Settings() #type:ignore


settings = _settings()