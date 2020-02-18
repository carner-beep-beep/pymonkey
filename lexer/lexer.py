import tok

class Lexer():
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next_position = self.position + 1
        self.char = self.source[self.position]

    def next_token(self):
        t = tok.Tok()
        
        self.skip_whitespace()

        if self.char == '=':
            if self.peek() == '=':
                char = self.char
                self.next_char()
                t.literal = char + self.char
                t.tok_type = tok.EQ
            else:
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
        elif self.char == '!':
            if self.peek() == '=':
                char = self.char
                self.next_char()
                t.literal = char + self.char
                t.tok_type = tok.NOT_EQ
            else:
                t.tok_type = tok.BANG
                t.literal = self.char
        elif self.char == '-':
            t.tok_type = tok.MINUS
            t.literal = self.char
        elif self.char == '/':
            t.tok_type = tok.SLASH
            t.literal = self.char
        elif self.char == '*':
            t.tok_type = tok.ASTERISK
            t.literal = self.char
        elif self.char == '>':
            t.tok_type = tok.GT
            t.literal = self.char
        elif self.char == '<':
            t.tok_type = tok.LT
            t.literal = self.char
        elif self.char == 0:
            t.tok_type = tok.EOF
            t.literal = ''
        else:
            if self.char.isalpha():
                print('In read identifier')
                t.literal = self.read_identifier()
                t.tok_type = tok.lookup_keyword(t.literal)
                return t  # return here so we don't update position
            elif self.char.isdigit():
                print('In read number')
                t.tok_type = tok.INT
                t.literal = self.read_number()
                return t
            else:
                tok.tok_type = tok.ILLEGAL
                tok.literal = self.char

        self.next_char()

        return t

    def next_char(self):
        self.position += 1
        if self.position >= len(self.source):
            self.char = 0   # EOF
        else:
            self.char = self.source[self.position]
            print(f'self.char: {self.char} is type {type(self.char)}')
            self.next_position = self.position + 1

    def read_identifier(self):
        start_position = self.position
        while self.char.isalpha():
            self.next_char()
        return self.source[start_position:self.position]

    def read_number(self):
        start_position = self.position
        while self.char.isdigit():
            self.next_char()
        return self.source[start_position:self.position]

    def skip_whitespace(self):
        if self.char == 0:
            return
        while self.char.isspace():
            self.next_char()

    def peek(self):
        if self.next_position >= len(self.source):
            return 0
        else:
            return self.source[self.next_position]

