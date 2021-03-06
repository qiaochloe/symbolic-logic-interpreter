from stmt import Expression
from expr import Expr, Binary, Unary, Grouping, Literal
from token_type import TokenType
from token import Token
from error_handler import ErrorHandler
from error import LoxRunTimeError
from visitor import Visitor

from scanner import Scanner
from parser import Parser


class Interpreter(Visitor):
    def __init__(self, error_handler):
        self.error_handler = error_handler

    def interpret(self, statements):
        try:
            for statement in statements:
                value = self.evaluate(statement.expr)
                return value
        except LoxRunTimeError as error:
            self.error_handler.runtime_error(error)

    def visit_expression_stmt(self, stmt):
        expr = self.evaluate(stmt.expr)

    def visit_literal_expr(self, expr):
        return False
        # return expr.value

    def visit_grouping_expr(self, expr):
        return self.evaluate(expr.expression)

    def visit_unary_expr(self, expr):
        right = self.evaluate(expr.right)
        if expr.operator.type_ == TokenType.NEG:
            return not right

    def visit_binary_expr(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.operator.type_:
            case TokenType.AND:
                return left and right
            case TokenType.OR:
                return left or right
            case TokenType.IMPLIES:
                return not (left is True and right is False)
            case TokenType.EQUIV:
                return left is right

    def execute(self, statement):
        statement.accept(self)

    def evaluate(self, expr):
        return expr.accept(self)


def main(expression):
    error = ErrorHandler()
    print(f"Expression: {expression}")

    print("\nScanner:")
    a = Scanner(error, expression)
    a_tokens = a.scan_tokens()
    for token in a_tokens:
        print(token)

    print("\nParser:")
    b = Parser(a_tokens, error)
    b_expr = b.parse()
    for expr in b_expr:
        print(expr)

    print("\nInterpreter:")
    interp = Interpreter(error)
    print(interp.interpret(b_expr))


main("M \land (E \lor D)")
