from parcours import RootedGraph

class semantic2RG:
    def __init__(self,semantic):
        self.semantic=semantic
    
    def root(self):
        return self.semantic.initial()
    
    def neighbors(self, state):
        actions = self.semantic.actions(state)
        voisins = []
        for action in actions:
            targets = self.semantic.execute(action,state)
            voisins.extend(targets)

