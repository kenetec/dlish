# dlish

Random data for the masses.

Write templates, create data.

dlish provides **Generators**. These **Generators** generate data.
dlish provides a **Unit Generator** which generates units of data created by **Generators**.
```python
user_template = {
    'name': strg.FromRegex(regex='[a-zA-Z]', minlen=2, maxlen=14),
    'age': intg.FromRange(10, 120),
    'email': strg.Email(namemin=5, providers=['gmail.com', 'yahoo.com']),
    'tags': listg.FromChoices(['happy', 'hungry', 'helpful', 'hellish'], minlen=2),

    'info': unitg.FromTemplate({
        'favorite_food': listg.FromChoices(['burger', 'apple', 'soda', 'cashew']),
        'favorite_num': intg.FromRange(0, 10),
    }),
}

gen = unitg.FromTemplate(user_template)

for user in gen.iter(5):
    print(repr(user))
```

### Common Generators
Most commonly depended upon generators
`strg.FromRegex`
`intg.FromRange`
`listg.FromChoices`
`unitg.FromTemplate`

## dlish template files
`.dsh` files