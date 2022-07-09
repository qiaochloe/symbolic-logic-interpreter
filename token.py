class Token:
    def __init__(self, type_, lexeme, literal, line):
        self.type_ = type_
        self.lexeme = lexeme
        self.literal = literal  # NOTE: Why does this exist?
        self.line = line

    def __str__(self):
        return f"{self.lexeme}"
