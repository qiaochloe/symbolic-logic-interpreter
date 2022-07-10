from token import Token


class ParseError(RuntimeError):
    def __init__(self, message):
        super().__init__(message)


class LoxRunTimeError(RuntimeError):
    def __init__(self, token: Token, message: str):
        super().__init__(message)
        self.token = token
