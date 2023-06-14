import json

import openai
from fastapi import Request, HTTPException, Response

from msg.chat_messages import ChatMessages
from utils.all_utils import build_stream_msg


async def chat_not_stream(api_key: str,
                          chat: ChatMessages) -> Response:
    openai.api_key = api_key
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
        raise HTTPException(status_code=500, detail=e)


async def chat_stream(
        request: Request,
        api_key: str,
        chat: ChatMessages):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model=chat.model,
            temperature=chat.temperature,
            presence_penalty=chat.presence_penalty,
            frequency_penalty=chat.frequency_penalty,
            stream=True,
            messages=chat.messages)
    except Exception as e:
        # yield build_stream_msg(e.http_body, True) if e.http_body is not None else build_stream_msg(e.user_message)\
        raise HTTPException(status_code=500, detail=e)
    else:
        for trunk in response:
            if await request.is_disconnected():
                break
            if trunk is None:
                continue
            if trunk['choices'][0]['finish_reason'] is not None:
                break
            else:
                yield json.dumps(trunk)
    finally:
        yield '[DONE]'
