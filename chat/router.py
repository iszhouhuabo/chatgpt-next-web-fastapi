import requests
from fastapi import APIRouter, Request
from sse_starlette import EventSourceResponse
from starlette.responses import JSONResponse

from chat.chat import chat_stream, chat_not_stream
from msg.chat_messages import ChatMessages
from msg.utils import get_path, get_headers

chat_router = APIRouter()


# 聊天
@chat_router.post("/v1/chat/completions")
async def completions(request: Request, ):
    chat_message = ChatMessages(data=await request.json())
    if chat_message.stream:
        return EventSourceResponse(
            chat_stream(request, chat_message))
    else:
        return JSONResponse(chat_not_stream(request, chat_message))


# 已经使用额度
@chat_router.get("/dashboard/billing/usage")
async def usage(request: Request):
    start_date = request.query_params.get("start_date")
    end_date = request.query_params.get("end_date")
    response = requests.get(
        get_path() + "/dashboard/billing/usage?start_date={}&end_date={}".format(start_date, end_date),
        headers=get_headers(request))
    return JSONResponse(response.json())


# 总额度
@chat_router.get("/dashboard/billing/subscription")
async def subscription(request: Request):
    response = requests.get(get_path() + "/dashboard/billing/subscription", headers=get_headers(request))
    return JSONResponse(response.json())
