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
