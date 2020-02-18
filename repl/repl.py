from lexer.lexer import Lexer
from lexer import tok

PROMPT = '>> '

def start_repl(stdin, stdout):
    while True:
        line = input(PROMPT)
        if line == 'exit':
            break
        l = Lexer(line)        
        done = False
        tokens = []
        while not done:
            token = l.next_token()
            if token.tok_type == tok.EOF:
                done = True
            tokens.append(token)
        for token in tokens:
            print(token)
