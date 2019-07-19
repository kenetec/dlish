'''from generators import strg, listg, unitg, intg

user_template = {
    'name': strg.FromRegex(regex='[a-zA-Z]', minlen=2, maxlen=14),
    'age': intg.FromRange(10, 120),
    'email': strg.Email(namemin=5, providers=['gmail.com', 'yahoo.com']),
    'tags': listg.FromChoices(['happy', 'hungry', 'helpful', 'hellish'], minlen=2, repeats=False),

    'info': unitg.FromTemplate({
        'favorite_food': listg.FromChoices(['burger', 'apple', 'soda', 'cashew']),
        'favorite_num': intg.FromRange(0, 10),
    }),
}

gen = unitg.FromTemplate(user_template)

for user in gen.iter(5):
    print(repr(user))
'''
'''
from interpreter import parser

p = parser.Parser('example.dsh')
p.go()
print(repr(p.tree.get_real()))
'''

from interpreter.lex import Lex, StopTokenizing

tokens = []

lex = Lex('example.dsh')

try:
    while True:
        tokens.append(lex.get_token())
except StopTokenizing:
    for tok in tokens:
        print(tok)