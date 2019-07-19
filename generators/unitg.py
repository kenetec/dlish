from .geng import Generator

class FromTemplate(Generator):
    """Generates data from key-to-Generator sets"""
    def __init__(self, template):
        self.template = template
    
    def gen(self):
        generated = {}
        for key, value in self.template.items():
            if isinstance(value, Generator):
                generated[key] = value.gen()
            else:
                generated[key] = value
        
        return generated