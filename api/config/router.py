from fastapi import APIRouter
from starlette.responses import JSONResponse

from settings.config import settings

config_router = APIRouter()


# 给前端的一些配置
@config_router.post("")
async def subscription() -> JSONResponse:
    return JSONResponse({"needCode": True if settings.code else False,
                         "hideUserApiKey": settings.hide_user_api_key,
                         "enableGPT4": not settings.disable_gpt4})
