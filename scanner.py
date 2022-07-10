from token import Token
from token_type import TokenType
from error_handler import ErrorHandler


class Scanner:
    def __init__(self, error_handler, source):
        self.source = source
        self.error_handler = error_handler

        self.tokens = []

        self.start = 0  # first char in lexeme
        self.current = 0
        self.line = 1  # line current is on

        self.keywords = {
            "\land": TokenType.AND,
            "\lor": TokenType.OR,
            "\lneg": TokenType.NEG,
            "\limplies": TokenType.IMPLIES,
            "\equiv": TokenType.EQUIV,
        }

        self.single_keys = {
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "[": TokenType.LEFT_BRACKET,
            "]": TokenType.RIGHT_BRACKET,
        }

    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        char = self.advance()

        if char in self.single_keys:
            self.add_token(self.single_keys.get(char))

        elif char in ["", " "]:  # spaces and empty strings
            pass

        elif char == "\n":  # newlines
            self.line += 1

        elif char == "\\":  # \ signifies start of operator
            self.identifier()

        elif self.is_alpha(char):
            if not self.is_alpha(self.peek()):
                self.add_token(TokenType.STATEMENT)

        else:
            self.error_handler.error(self.line, "Unexpected character.")

    def peek(self):
        if self.is_at_end():
            return "\0"  # What?
        return self.source[self.current]

    def is_alpha(self, char):
        return (char >= "a" and char <= "z") or (char >= "A" and char <= "Z")

    def identifier(self):
        while self.is_alpha(self.peek()):
            self.advance()

        text = self.source[self.start : self.current]
        if text in self.keywords:
            type_ = self.keywords[text]
            self.add_token(type_)
        else:
            self.error_handler_error(self.line, "Unknown operator.")

    def advance(self):
        char = self.peek()
        self.current += 1
        return char

    def add_token(self, type_, literal=None):
        lexeme = self.source[self.start : self.current]
        self.tokens.append(Token(type_, lexeme, literal, self.line))

    # def match(self, *expected):
    #    if self.is_at_end():
    #        return False

    #    for char in expected:
    #        if self.source[current] == expected:
    #            self.current += 1
    #            return True

    #    return False
