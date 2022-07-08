from token import Token
from token_type import TokenType


class ErrorHandler:
    def __init__(self):
        self.had_error = False

    def error(self, line, message):
        self.report(line, "", message)

    def error_on_token(self, token, message):
        if token.type == TokenType.EOF:
            self.report(toke.line, "at end", message)
        else:
            self.report(token.line, f" at '{token.lexeme}'", message)

    def report(self, line, where, message):
        print(f"[line {line}] Error {where}: {message}")
        self.had_error = True
