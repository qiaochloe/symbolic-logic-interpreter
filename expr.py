class Expr:
    pass


class Literal(Expr):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_literal_expr(self)

    def __str__(self):
        return f"{self.value}"


class Unary(Expr):
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_unary_expr(self)

    def __str__(self):
        return f"{self.operator} {self.right}"


class Binary(Expr):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_binary_expr(self)

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"


class Grouping(Expr):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_grouping_expr(self)

    def __str__(self):
        return f"({self.expression})"
