import json
import os
import time

from fastapi import HTTPException

from api.auth import auth_headers


def build_msg(msg):
    if msg is not None:
        return {"choices": [{"message": {"content": f"{msg}"}}]}
    return {"choices": [{"message": {"content": "不知道的错误,请稍后再试!"}}]}


def build_stream_msg(msg, is_json: bool = False):
    if msg is not None:
        if "Rate limit reached" in msg:
            format_msg = "系统过载, 请稍后再试! `rate limit`"
        else:
            format_msg = f"```json \n{msg}```" if is_json else msg
        return json.dumps(
            {"choices": [{"delta": {"content": f"{format_msg}"}}]})
    return json.dumps({"choices": [{"delta": {"content": "不知道的错误,请稍后再试!"}}]})


def get_path():
    open_path = os.getenv("BASE_URL")
    return open_path if open_path else "https://api.openai.com"


def get_headers(authorization: str):
    openai_headers = {
        "Content-Type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "Authorization": "",
    }
    auth_rep = auth_headers(authorization)

    if auth_rep["error"]:
        raise HTTPException(status_code=401, detail=auth_rep["message"])

    openai_headers["Authorization"] = f"Bearer {auth_rep['api_key']}"

    return openai_headers


def get_now():
    timestamp = time.time()
    time_tuple = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
