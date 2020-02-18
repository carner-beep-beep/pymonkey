from .tok import Tok
from . import tok
from .lexer import Lexer

def test_tokens():
    program_input = '''let five = 5;
    let ten = 10;

    let add = fn(x, y) {
        x + y;
    };

    let result = add(five, ten);
    !-/*5;
    5 < 10 > 5;

    if (5 < 10) {
        return true;
    } else {
        return false;
    }

    10 == 10;
    10 != 9;'''

    expected_tokens = [
            Tok(tok.LET, 'let'),
            Tok(tok.IDENT, 'five'),
            Tok(tok.ASSIGN, '='),
            Tok(tok.INT, '5'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.LET, 'let'),
            Tok(tok.IDENT, 'ten'),
            Tok(tok.ASSIGN, '='),
            Tok(tok.INT, '10'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.LET, 'let'),
            Tok(tok.IDENT, 'add'),
            Tok(tok.ASSIGN, '='),
            Tok(tok.FUNCTION, 'fn'),
            Tok(tok.LPAREN, '('),
            Tok(tok.IDENT, 'x'),
            Tok(tok.COMMA, ','),
            Tok(tok.IDENT, 'y'),
            Tok(tok.RPAREN, ')'),
            Tok(tok.LBRACE, '{'),
            Tok(tok.IDENT, 'x'),
            Tok(tok.PLUS, '+'),
            Tok(tok.IDENT, 'y'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.RBRACE, '}'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.LET, 'let'),
            Tok(tok.IDENT, 'result'),
            Tok(tok.ASSIGN, '='),
            Tok(tok.IDENT, 'add'),
            Tok(tok.LPAREN, '('),
            Tok(tok.IDENT, 'five'),
            Tok(tok.COMMA, ','),
            Tok(tok.IDENT, 'ten'),
            Tok(tok.RPAREN, ')'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.BANG, '!'),
            Tok(tok.MINUS, '-'),
            Tok(tok.SLASH, '/'),
            Tok(tok.ASTERISK, '*'),
            Tok(tok.INT, '5'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.INT, '5'),
            Tok(tok.LT, '<'),
            Tok(tok.INT, '10'),
            Tok(tok.GT, '>'),
            Tok(tok.INT, '5'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.IF, 'if'),
            Tok(tok.LPAREN, '('),
            Tok(tok.INT, '5'),
            Tok(tok.LT, '<'),
            Tok(tok.INT, '10'),
            Tok(tok.RPAREN, ')'),
            Tok(tok.LBRACE, '{'),
            Tok(tok.RETURN, 'return'),
            Tok(tok.TRUE, 'true'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.RBRACE, '}'),
            Tok(tok.ELSE, 'else'),
            Tok(tok.LBRACE, '{'),
            Tok(tok.RETURN, 'return'),
            Tok(tok.FALSE, 'false'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.RBRACE, '}'),
            Tok(tok.INT, '10'),
            Tok(tok.EQ, '=='),
            Tok(tok.INT, '10'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.INT, '10'),
            Tok(tok.NOT_EQ, '!='),
            Tok(tok.INT, '9'),
            Tok(tok.SEMICOLON, ';'),
            Tok(tok.EOF, '')
    ]
    
    lexer = Lexer(program_input)

    for expected_token in expected_tokens:
        token = lexer.next_token()
        assert token.tok_type == expected_token.tok_type
        assert token.literal == expected_token.literal
