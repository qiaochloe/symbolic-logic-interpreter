from token_type import TokenType
from token import Token

from scanner import Scanner
from error_handler import ErrorHandler
from stmt import Expression
from expr import Literal, Unary, Binary, Grouping
from visitor import Visitor


class Parser:
    def __init__(self, tokens, error_handler):
        self.tokens = tokens
        self.error_handler = error_handler
        self.current = 0
        self.loop_depth = 0  # Don't actually need this

    def parse(self):
        statements = []
        # count = 0
        # while not self.is_at_end():
        #    statements.append(self.declaration())
        #    print(count)
        #    count += 1

        statements.append(self.declaration())
        return statements

    # BYPASSED declaration, expression_statement()
    def declaration(self):
        return self.expression_statement()

    def expression_statement(self):
        expr = self.expression()
        return Expression(expr)

    def match(self, *token_types):
        for type_ in token_types:
            if self.check(type_):
                self.advance()
                return True
        return False

    # expression -> binary
    def expression(self):
        return self.binary()

    # binary -> unary (("\land" | "\lor" | "\limplies" | "\equiv") unary)* ;
    def binary(self):
        expr = self.unary()
        if self.match(  # not while
            TokenType.AND, TokenType.OR, TokenType.IMPLIES, TokenType.EQUIV
        ):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self):
        if self.match(TokenType.NEG):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(TokenType.STATEMENT):
            return Literal(self.previous().lexeme)
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        self.error_handler.error_on_token(self.peek(), "Expect expression.")

    def check(self, type_):
        if self.is_at_end():
            return False
        return self.peek().type_ == type_

    def is_at_end(self):
        return self.peek().type_ == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def previous(self):
        return self.tokens[self.current - 1]

    def consume(self, type_, message):
        if self.check(type_):
            return self.advance()
        self.error(self.peek(), message)

    def error(self, token, message):
        self.error_handler.error_on_token(token, message)
        # return ParseError("")
