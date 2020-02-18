
# Constants
ILLEGAL = 'ILLEGAL'
EOF     = 'EOF'

IDENT   = 'IDENT'
INT     = 'INT'

# Operators
ASSIGN  = '='
PLUS    = '+'
MINUS   = '-'
BANG    = '!'
SLASH   = '/'
ASTERISK = '*'

GT      = '>'
LT      = '<'

EQ      = '=='
NOT_EQ  = '!='

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
TRUE     = 'TRUE'
FALSE    = 'FALSE'
IF       = 'IF'
ELSE     = 'ELSE'
RETURN   = 'RETURN'

keywords = {'let': LET, 'fn': FUNCTION, 'true': TRUE, 'false': FALSE, 'if': IF,
        'else': ELSE, 'return': RETURN}

class Tok():
    def __init__(self, tok_type=None, literal=None):
        self.tok_type = tok_type
        self.literal = literal

    def __repr__(self):
        return f'Tok[type: {self.tok_type}, literal: {self.literal}]'

def lookup_keyword(ident):
    keyword = keywords.get(ident)
    if keyword:
        return keyword
    return IDENT
