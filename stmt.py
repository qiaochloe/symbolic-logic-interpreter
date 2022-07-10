class Stmt:
    pass


class Expression(Stmt):
    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visit_expression_stmt(self)

    def __str__(self):
        return f"(STATEMENT: {self.expr})"
