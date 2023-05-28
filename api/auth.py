import os

from constant import access_code_prefix


def auth_headers(authorization: str) -> {bool, str}:
    authorize_code = os.getenv("CODE")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if authorize_code is None:
        return {"error": False, "message": "Not Open code model", "api_key": openai_api_key}

    if authorization is None:
        return {"error": True, "message": "No Authorization header provided"}

    api_key_or_code = authorization.removeprefix("Bearer ")

    if not api_key_or_code.startswith(access_code_prefix):
        return {"error": False, "message": "You have key", "api_key": api_key_or_code}

    if api_key_or_code.removeprefix(access_code_prefix) in authorize_code.split(","):
        return {"error": False, "message": "Use System api key", "api_key": openai_api_key}

    return {"error": True, "message": "Invalid Authorization header provided"}
