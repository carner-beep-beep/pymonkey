import tok

class Lexer():
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next_position = self.position + 1
        self.char = self.source[self.position]

    def next_token(self):
        t = tok.Tok()

        if self.char == '=':
            t.tok_type = tok.ASSIGN
            t.literal = self.char
        elif self.char == '+':
            t.tok_type = tok.PLUS
            t.literal = self.char
        elif self.char == ',':
            t.tok_type = tok.COMMA
            t.literal = self.char
        elif self.char == ';':
            t.tok_type = tok.SEMICOLON
            t.literal = self.char
        elif self.char == '(':
            t.tok_type = tok.LPAREN
            t.literal = self.char
        elif self.char == ')':
            t.tok_type = tok.RPAREN
            t.literal = self.char
        elif self.char == '{':
            t.tok_type = tok.LBRACE
            t.literal = self.char
        elif self.char == '}':
            t.tok_type = tok.RBRACE
            t.literal = self.char

        self.next_char()

        return t

    def next_char(self):
        self.position += 1
        if self.position >= len(self.source):
            self.char = 0   # EOF
        else:
            self.char = self.source[self.position]
            self.next_position = self.position + 1
