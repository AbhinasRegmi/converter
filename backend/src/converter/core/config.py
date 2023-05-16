from typing import List
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    MONGODB_DB_NAME: str = "converter"

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