class Piece:
    def __init__(self, name, garde, action):
        #list, lambda, lambda
        self.name = name
        self.garde = garde
        self.action = action
    
    def garde(self):
        return self.garde
    
    def action(self):
        return self.action 

    def enabled(self,c):
        return self.garde(c)
    
    def execute(self, c):
        return [self.action(c)]
