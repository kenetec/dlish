"""
dlish string generator

### Includes:\n
`FromRegex(regex='', minlen=1, maxlen=1)`
"""
from .geng import Generator
import random
import re
import string
from .listg import FromChoices

ALL_CHARS = string.ascii_letters + string.digits + r'`-=[]\;\',./~!@#$%^&*()_+{}|:"<>?'
LEN_OF_ALL_CHARS = len(ALL_CHARS)

class FromRegex(Generator):
    """String generator that generates based on regex."""
    
    def __init__(self, regex='', minlen=1, maxlen=1):
        self.regex = re.compile(regex)
        self.minlen = minlen
        self.maxlen = (maxlen >= minlen and maxlen or minlen)
        # self.weights = kwargs['weights'] or {}

    
    def gen(self):
        """Generates data."""
        generated = ''
        # start with a random letter
        generated = generated + string.ascii_letters[random.randrange(0, len(string.ascii_letters))]

        while len(generated) < self.minlen:
            chosen = ALL_CHARS[random.randrange(0, LEN_OF_ALL_CHARS)]

            while not self.regex.match(chosen):
                chosen = ALL_CHARS[random.randrange(0, LEN_OF_ALL_CHARS)]
            
            generated = generated + chosen

        # random range between minlen & maxlen
        max_chars = random.randint(self.minlen, self.maxlen)
        while len(generated) < max_chars:
            chosen = ALL_CHARS[random.randrange(0, LEN_OF_ALL_CHARS)]

            while not self.regex.match(chosen):
                chosen = ALL_CHARS[random.randrange(0, LEN_OF_ALL_CHARS)]
            
            generated = generated + chosen
        
        return generated


class Email(Generator):
    """Email generator"""
    def __init__(self, providers=[], namemin=1, namemax=1):
        self.namemin = namemin
        self.namemax = namemax
        self.provider_gen = FromChoices(providers)
        self.from_regex_gen = FromRegex('[a-zA-Z0-9]', namemin, namemax)
    
    def gen(self):
        name = self.from_regex_gen.gen()
        provider = ''.join(self.provider_gen.gen())
        return name + '@' + provider


