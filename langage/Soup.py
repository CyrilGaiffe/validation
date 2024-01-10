from abc import ABC

class SoupConfiguration(ABC):
    def __init__(self):
        pass

    def __eq__(self, other):
        pass
    
    def __hash__(self):
        pass

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


class SoupSpec:
    def __init__(self, initial, pieces):
        self.initial = initial
        self.pieces = pieces
    

    def initial(self):
        return self.initial
    
    def pieces(self):
        return self.pieces
    
    def enabledPieces(self, c):
        return [piece for piece in self.pieces if piece.enabled(c)]

    
class SoupSemantics:
    def __init__(self, soupSpec):
        self.soupSpec = soupSpec

    def initial(self):
        return self.soupSpec.initial()
    
    def actions(self, c):
        return self.soupSpec.enabledPieces.action(c)
    
    def execute(self, p, c):
        return p.execute(c)