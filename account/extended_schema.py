unauthorized_schema = {
    "type": "object",
    "properties": {
        "detail": {"type": "string"},
        "code": {"type": "string"},
        "messages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "token_class": {"type": "string"},
                    "token_type": {"type": "string"},
                    "message": {"type": "string"},
                },
            },
        },
    },
    "example": {
        "detail": "Given token not valid for any token type",
        "code": "token_not_valid",
        "messages": [
            {
                "token_class": "AccessToken",
                "token_type": "access",
                "message": "Token is invalid or expired",
            }
        ],
    },
}


logout_schema = {
    204: {
        "type": "object",
        "properties": {"message": {"type": "string"}},
        "example": {"message": "Logged out successfully"},
    },
    401: {**unauthorized_schema},
}