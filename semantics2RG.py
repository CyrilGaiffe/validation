
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


# use : semantic2RG(semantic)
# semantic2RG(semantic).root()
# semantic2RG(semantic).neighbors(state)
# allows to use a semantic as a rooted graph