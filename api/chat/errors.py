def handler(error: Exception):
    if error is None:
        return None
    # open ai error sts and msg
    http_status = error.http_status
    http_body = error.http_body if error.http_body is not None else error.user_message

    if http_status == 401:
        return "没有输入正确的密钥! \n{}".format(http_body)
    if http_status == 443:
        return "AI 忙不过来了,请稍后再试!"
    if "Connection aborted" in http_body or "Connection reset by peer" in http_body:
        return "AI 不小心下线了,请稍后再试!"
    if "No API key provided" in http_body:
        return "没有设置 API KYE!"
    return http_body
