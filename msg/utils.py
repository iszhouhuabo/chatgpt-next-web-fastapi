import json
import os
import time

from fastapi import Request


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


def get_headers(request: Request):
    headers = {
        "Content-Type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "Authorization": "",
    }
    token = request.headers["Authorization"].removeprefix("Bearer ") if "Authorization" in request.headers else None

    # use user's api key first
    if token and "ak-" not in token:
        headers["Authorization"] = f"Bearer {token}"
    else:
        authorize_code = os.getenv("CODE")
        if not authorize_code or token.removeprefix("ak-") in authorize_code.split(","):
            headers["Authorization"] = f"Bearer {os.getenv('OPENAI_API_KEY')}"
    return headers


def get_now():
    timestamp = time.time()
    time_tuple = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
