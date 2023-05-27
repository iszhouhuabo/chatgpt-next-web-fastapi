import os

from fastapi import APIRouter
from starlette.responses import JSONResponse

config_router = APIRouter()


# 总额度
@config_router.post("")
async def subscription() -> JSONResponse:
    return JSONResponse({"needCode": True if os.getenv("CODE") not in ("", None) else False,
                         "hideUserApiKey": True if os.getenv("HIDE_USER_API_KEY") is 1 else False,
                         "enableGPT4": True if os.getenv("HIDE_USER_API_KEY") is 1 else False})
