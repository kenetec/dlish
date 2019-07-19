"""
dlish generic generator
"""
class Iterator:
    """Generic iterator for generators."""
    def __init__(self, gen, times):
        self.max = times
        self.gen = gen
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max > 0:
            if self.current < self.max:
                self.current = self.current + 1
                return self.gen.gen()
            else:
                raise StopIteration
        else:
            return self.gen.gen()

class Generator:
    """Generic generator class."""
    def __init__(self):
        pass

    def iter(self, times):
        """Creates an iterator that will run the specified amount of times given."""
        return Iterator(self, times)
    
    def make(self, amount):
        """Makes a list of generated data."""
        results = []

        for _ in range(amount):
            results.append(self.gen())
        
        return results
    
    def gen(self):
        """Generates data."""
        raise NotImplementedError