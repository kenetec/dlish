from .tree import Tree
import interpreter.lex as lex

'''
{
    user: {
        name: {
            type: 'str',
            regex: '[a-zA-Z]',
            len: [3, 10]
        }
    }
}
'''

class Parser:
    '''
    decl            =       ID  ':' '\n'        |
                                    'str'       |
                                    'list'      |
                                    'int'       |
                                    string_exp  |
                                    list_exp

    list_exp        =       '[' [(string_exp | NUM) ',']... ']'

    string_exp      =       '\''|'"'    [content]  '\''|'"'
    '''
    def __init__(self, input_fp):
        self.lex = lex.Lex(input_fp)
        self.tree = Tree()
        self.current_tabs = 0

    def go(self):
        self.lex.next_char()
        self.token = self.lex.get_token()
        self.decl()
    
    def found(self, token_type):
        if self.token.token_type == token_type:
            return True
        else:
            return False
    
    def consume(self, token_type):
        if self.token.token_type == token_type:
            consumed = self.token

            try:
                self.token = self.lex.get_token()
            except lex.StopTokenizing:
                print('STOP TOKENIZING')
            
            return consumed

    def decl(self):
        name = self.consume('ID')
        self.consume(':')

        if self.found('\n'):
            self.consume('\n')
            # get tabs of new line
            new_tabs = 0
            while self.found('\t'):
                self.consume('\t')
                new_tabs = new_tabs + 1

            if new_tabs < self.current_tabs:
                # exit branch
                diff = self.current_tabs - new_tabs

                for _ in range(diff):
                    self.tree.exit_branch()
                
                # decl
                self.decl()
            elif new_tabs == self.current_tabs:
                # error bc a type name is missing
                print('new_tabs == self.current_tabs')
                pass
            else:
                self.current_tabs = new_tabs
                # new branch
                self.tree.new_branch(name)
                # decl
                self.decl()
        elif self.found('\'') or self.found('"'):
            # string expression
            # leaf
            self.tree.new_leaf(name, self.string_exp())
        elif self.found('['):
            # list expression or array
            self.consume('[')

            while not self.found(']'):
                try:
                    self.token = self.lex.get_token()
                except lex.StopTokenizing:
                    pass
            
            self.consume(']')
            # leaf
            pass
        elif self.found('NUM'):
            # number
            n = int(self.consume('NUM'))
            self.tree.new_leaf(name, n)
        else:
            # type
            dt = self.consume('ID')
            # leaf
            self.tree.new_leaf(name, dt)
            
    
    def string_exp(self):
        quote_char = ''
        if self.found('\''):
            quote_char = self.consume('\'')
        elif self.found('"'):
            quote_char = self.consume('"')
        
        s = ''
        while not self.found(quote_char):
            s = s + self.consume('ID')
        
        # consume quote char
        self.consume(quote_char) 

        return s
    
    def list_exp(self):
        pass

