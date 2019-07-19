from .geng import Generator
import random

class FromRange(Generator):
    """Generates numbers based off of nmin and nmax.\n
    *behaves same as random.randrange*
    """
    def __init__(self, nmin, nmax=0):
        self.nmin = nmin
        self.nmax = nmax >= nmin and nmax or nmin
    
    def gen(self):
        return random.randrange(self.nmin, self.nmax)