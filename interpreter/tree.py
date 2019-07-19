import copy

class Branch:
    def __init__(self, parent):
        self.parent = parent
        self.leaves = {}
        self.sub_branches = {}
    
    def new_leaf(self, name, val):
        self.leaves[name] = val
    
    def new_branch(self, name):
        self.sub_branches[name] = Branch(self)
        return self.sub_branches[name]

class Tree:
    def __init__(self):
        self.root = Branch(None)
        self.current = self.root
    
    def new_branch(self, name):
        self.current = self.current.new_branch(name)
    
    def exit_branch(self):
        if self.current.parent != None:
            self.current = self.current.parent
    
    def new_leaf(self, name, val):
        self.current.new_leaf(name, val)

    def get_real(self):
        # make a template of generators
        def recurse(branch):
            result = copy.deepcopy(branch.leaves)

            for key, val in branch.leaves.items():
                pass

            for name, sub_branch in branch.sub_branches.items():
                result[name] = recurse(sub_branch)
            
            return result
        
        return recurse(self.root)