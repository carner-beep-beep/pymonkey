
# Constants
ILLEGAL = 'ILLEGAL'
EOF     = 'EOF'

IDENT   = 'IDENT'
INT     = 'INT'

# Operators
ASSIGN  = '='
PLUS    = '+'

# Delimiters
COMMA   = ','
SEMICOLON = ';'

LPAREN  = '('
RPAREN  = ')'
LBRACE  = '{'
RBRACE  = '}'

# Keywords
FUNCTION = 'FUNCTION'
LET      = 'LET'

class Tok():
    def __init__(self, tok_type, literal):
        self.tok_type = tok_type
        self.literal = literal

    def __repr__(self):
        return f'Tok[type: {self.tok_type}, literal: {self.literal}]'
