import json
import os

import openai
from fastapi import Request

from msg.chat_messages import ChatMessages
from msg.utils import build_stream_msg, build_msg


def pre_check(request: Request):
    authorize_code = os.getenv("CODE")
    if "Authorization" in request.headers:
        bearer = request.headers["Authorization"]
        if authorize_code is not None:
            if bearer is None:
                return
            elif "Bearer ak-" in bearer:
                if bearer[10:] in authorize_code.split(","):
                    return os.getenv("OPENAI_API_KEY")
                return
            else:
                return bearer[7:]
        elif "Bearer ak-" not in bearer:
            return bearer[7:]
        else:
            return
    elif authorize_code is not None:
        return
    else:
        return os.getenv("OPENAI_API_KEY")


def chat_not_stream(request: Request,
                    chat: ChatMessages):
    api_key = pre_check(request)
    if api_key is None:
        return build_msg("管理员已经开启授权模式, 请输入授权码或使用自己的 OpenAI API Key")
    try:
        response = openai.ChatCompletion.create(
            model=chat.model,
            temperature=chat.temperature,
            presence_penalty=chat.presence_penalty,
            frequency_penalty=chat.frequency_penalty,
            stream=False,
            messages=chat.messages)
        return response
    except Exception as e:
        return json.dumps(e)


async def chat_stream(
        request: Request,
        chat: ChatMessages):
    api_key = pre_check(request)
    if api_key is None:
        yield build_stream_msg("管理员已经开启授权模式, 请输入授权码或使用自己的 OpenAI API Key")
        yield '[DONE]'
        return
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model=chat.model,
            temperature=chat.temperature,
            presence_penalty=chat.presence_penalty,
            frequency_penalty=chat.frequency_penalty,
            stream=chat.stream,
            messages=chat.messages)
    except Exception as e:
        yield build_stream_msg(e.http_body, True) if e.http_body is not None else build_stream_msg(e.user_message)
        yield '[DONE]'
        return

    for trunk in response:
        if await request.is_disconnected():
            break
        if trunk['choices'][0]['finish_reason'] is not None:
            data = '[DONE]'
        else:
            data = json.dumps(trunk)
        yield data
