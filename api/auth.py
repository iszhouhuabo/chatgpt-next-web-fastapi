import os

from constant import access_code_prefix
from settings.config import settings


def auth_headers(authorization: str) -> {bool, str}:
    authorize_code = os.getenv("CODE")

    if settings.code is None:
        return {"error": False, "message": "Not Open code model", "api_key": settings.openai_api_key}

    if authorization is None:
        return {"error": True, "message": "No Authorization header provided"}

    api_key_or_code = authorization.removeprefix("Bearer ")

    if not api_key_or_code.startswith(access_code_prefix):
        return {"error": False, "message": "You have key", "api_key": api_key_or_code}

    if api_key_or_code.removeprefix(access_code_prefix) in authorize_code.split(","):
        return {"error": False, "message": "Use System api key", "api_key": settings.openai_api_key}

    return {"error": True, "message": "Invalid Authorization header provided"}
