class SoupSemantics:
    def __init__(self, soupSpec):
        self.soupSpec = soupSpec

    def initial(self):
        return self.soupSpec.initial()
    
    def actions(self, c):
        return self.soupSpec.enabledPieces(c)
    
    def execute(self, p, c):
        return p.execute(c)
