from .geng import Generator
import random

class FromChoices(Generator):
    """List generator that generates based on given choices and length"""
    def __init__(self, choices=[], minlen=1, maxlen=1, repeats=True):
        self.choices = choices
        self.choices_len = len(choices)
        self.minlen = minlen
        self.maxlen = (maxlen >= minlen and maxlen or minlen)
        self.repeats = repeats
    
    def gen(self):
        generated = []
        
        while len(generated) < self.minlen:
            chosen = self.choices[random.randrange(0, self.choices_len)]
            
            if chosen in generated and self.repeats == False:
                while chosen in generated:
                    chosen = self.choices[random.randrange(0, self.choices_len)]

            generated.append(chosen)
        
        # random range between minlen & maxlen
        max_size = random.randint(self.minlen, self.maxlen)

        while len(generated) < max_size:
            chosen = self.choices[random.randrange(0, self.choices_len)]

            if chosen in generated and self.repeats == False:
                while chosen in generated:
                    chosen = self.choices[random.randrange(0, self.choices_len)]
                    
            generated.append(chosen)
        
        return generated