def error_response(message: str, code: int):
    return {
        "error": {
            "message": message,
            "code": code
        }
    }