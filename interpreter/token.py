class TokenType:
    ID = 'ID'
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    REGEX = 'REGEX'
    COMMA = 'COMMA'
    L_BRACKET = 'LEFT BRACKET'
    R_BRACKET = 'RIGHT BRACKET'
    COLON = 'COLON'
    SEMICOLON = 'SEMICOLON'
    NEW_LINE = 'NEW LINE'
    TAB = 'TAB'

class Token:
    def __init__(self, token_type, lexme, source_index):
        self.token_type = token_type
        self.lexme = lexme
        self.source_index = source_index
    
    def __str__(self):
        if (self.token_type == TokenType.NEW_LINE or self.token_type == TokenType.TAB):
            return self.token_type + "\t\t" + str(self.source_index)
        return self.token_type + "\t" + self.lexme + "\t" + str(self.source_index)