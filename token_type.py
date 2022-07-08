from enum import Enum

TokenType = Enum(
    "TokenType",
    "LEFT_PAREN RIGHT_PAREN LEFT_BRACKET RIGHT_BRACKET \
    AND OR NEG IMPLIES EQUIV \
    STATEMENT \
    EOF",
)

# this depends on all of the keywords being back to back
# and taking values in the range `[23, 39)`
# RESERVED_KEYWORDS = {
#    TokenType(n).name.lower(): TokenType(n) for n in range(23, 38)}
