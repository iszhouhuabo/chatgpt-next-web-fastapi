# 全局配置信息
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: Optional[str]
    code: Optional[str]
    proxy_url: Optional[str]

    base_url: str = 'https://api.openai.com'
    openai_org_id: Optional[str]

    hide_user_api_key: Optional[bool] = False
    disable_gpt4: Optional[bool] = False

    class Config:
        env_file = ".env"

    @lru_cache(maxsize=None)
    def get(self, name: str):
        return getattr(self, name)


settings = Settings()
