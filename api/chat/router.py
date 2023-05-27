import requests
from fastapi import APIRouter, Request, Header, HTTPException
from sse_starlette import EventSourceResponse
from starlette.responses import JSONResponse

from api.auth import auth_headers
from api.chat.chat import chat_stream, chat_not_stream
from msg.chat_messages import ChatMessages
from utils.all_utils import get_path, get_headers

chat_router = APIRouter()


# 聊天
@chat_router.post("/v1/chat/completions")
async def completions(request: Request, authorization: str = Header(None)):
    chat_message = ChatMessages(data=await request.json())

    auth_rep = auth_headers(authorization)

    if auth_rep["error"]:
        raise HTTPException(status_code=401, detail=auth_rep["message"])

    if chat_message.stream:
        return EventSourceResponse(
            chat_stream(request, auth_rep["api_key"], chat_message))
    else:
        return JSONResponse(chat_not_stream(auth_rep["api_key"], chat_message))


# 已经使用额度
@chat_router.get("/dashboard/billing/usage")
async def usage(start_date: str, end_date: str, authorization: str = Header(None)):
    response = requests.get(
        get_path() + "/dashboard/billing/usage?start_date={}&end_date={}".format(start_date, end_date),
        headers=get_headers(authorization))
    return JSONResponse(response.json())


# 总额度
@chat_router.get("/dashboard/billing/subscription")
async def subscription(authorization: str = Header(None)):
    response = requests.get(get_path() + "/dashboard/billing/subscription", headers=get_headers(authorization))
    return JSONResponse(response.json())
