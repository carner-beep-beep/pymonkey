from tok import Tok
import tok
from lexer import Lexer

def test_tokens():
    program_input = '=+(){},;'

    expected_tokens = [
            Tok(tok.ASSIGN, '*'),
            Tok(tok.PLUS, '+'),
            Tok(tok.LPAREN, '('),
            Tok(tok.RPAREN, ')'),
            Tok(tok.LBRACE, '{'),
            Tok(tok.RBRACE, '}'),
            Tok(tok.COMMA, ','),
            Tok(tok.SEMICOLON, ';')
    ]
    
    lexer = Lexer(program_input)

    for expected_token in expected_tokens:
        token = lexer.next_token()
        assert token.tok_type == expected_token.tok_type
        assert token.literal == expected_token.literal
