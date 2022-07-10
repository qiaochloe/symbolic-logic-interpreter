from stmt import Expression
from expr import Expr, Binary, Unary, Grouping, Literal
from token_type import TokenType
from token import Token
from error_handler import ErrorHandler
from visitor import Visitor

from scanner import Scanner
from parser import Parser

# TODO: Fix accept() bug

class Interpreter(Visitor):
    def interpret(self, statements):
        for statement in statements:
            value = self.evaluate(statement.expr)
            print(value)
            #statement.accept(self)

    def visit_expression_stmt(self, stmt: Expression):
        expr = self.evaluate(stmt.expr)

    def visit_literal_expr(self, expr):
        return expr.value

    def visit_grouping_expr():
        return self.evaluate(expr.expression)

    def visit_unary_expr(self, expr):
        right = self.evaluate(expr.right)
        if expr.operator.type_ == TokenType.NEG:
            return not right

    def visit_binary_expr(self, expr):
        left = evaluate(expr.left)
        right = evaluate(expr.right)
        
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

error = ErrorHandler()
a = Scanner(error, "M \land (E \lor D)")
a_tokens = a.scan_tokens()
b = Parser(a_tokens, error)

b_terms = b.parse()
for term in b_terms:
    print(term)

interp = Interpreter()
print(interp.evaluate(b_terms))