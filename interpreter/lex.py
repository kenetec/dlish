import string
import sys
from interpreter.token import Token, TokenType

ALL_CHARS = string.ascii_letters + string.digits + r'_-!'
SYMBOLS = ['[', ']', ',', '\n', '\t', ':', '\'', '"', '`']

class StopTokenizing(Exception):
    '''
    Raised from calling Lex.get_token() when all tokens are exhausted.
    '''
    pass

class InvalidPeek(Exception):
    '''
    Raised when calling Lex.peek() with an offset that exceeds the length of the source.
    '''
    pass

class InvalidSyntax(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

class Lex:
    def __init__(self, filepath):
        file = open(filepath)
        self.source = ''.join(file.readlines())
        file.close()

        self.source_index = -1
        self.char = ''

    
    def next_char(self):
        if (self.source_index + 1) < len(self.source):
            self.source_index = self.source_index + 1
            self.char = self.source[self.source_index]
        else:
            raise StopTokenizing

    def peek(self, offset=1):
        peek_to = self.source_index + offset

        if peek_to < len(self.source):
            return self.source[peek_to]
        else:
            raise InvalidPeek
    
    def err(self, tok):
        # resolve source_index from source
        pass
    
    def get_token(self):
        if self.char in SYMBOLS:
            # build string
            if self.char == '\'' or self.char == '"' or self.char == '`':
                start_char = self.char
                start_index = self.source_index
                self.next_char() # start of string

                s = ""

                while (self.char != start_char):
                    s += self.char
                    self.next_char()
                
                # self.char == start_char
                if self.char == '\'' or self.char == '"':
                    self.next_char()
                    return Token(TokenType.STRING, s, start_index)
                elif self.char == '`':
                    self.next_char()
                    return Token(TokenType.REGEX, s, start_index)
                else:
                    raise InvalidSyntax

            # special character
            tok_type = self.char

            # reso
            if self.char == '[':
                tok_type = TokenType.L_BRACKET
            elif self.char == ']':
                tok_type = TokenType.R_BRACKET
            elif self.char == ':':
                tok_type = TokenType.COLON
            elif self.char == ";":
                tok_type = TokenType.SEMICOLON
            elif self.char == ",":
                tok_type = TokenType.COMMA
            elif self.char == '\n':
                tok_type = TokenType.NEW_LINE
            elif self.char == '\t':
                tok_type = TokenType.TAB

            tok = Token(tok_type, self.char, self.source_index)
            # next char
            self.next_char()
            return tok
        elif self.char in string.digits:
            # number
            start_index = self.source_index
            lexme = self.char

            # get next char
            self.next_char()

            while self.char in string.digits:
                lexme = lexme + self.char
                self.next_char()

            # return token
            return Token(TokenType.NUMBER, lexme, start_index)
        elif self.char in string.ascii_letters:
            # identifier
            start_index = self.source_index
            lexme = self.char

            # get next char
            self.next_char()

            while self.char in ALL_CHARS:
                lexme = lexme + self.char
                self.next_char()

            # return token
            return Token(TokenType.ID, lexme, start_index) 
        elif self.char == ' ':
            # get tab from spaces(4)
            i = 1
            while self.char == ' ':
                if i < 4:
                    i += 1
                    self.next_char()
                elif i == 4:
                    break
            
            if i == 4:
                return Token(TokenType.TAB, '\t', self.source_index)
            else:
                # ignore whitespace and call get_token
                return self.get_token()
        else:
            print('Unknown symbol: ' + repr(self.char))
            raise StopTokenizing