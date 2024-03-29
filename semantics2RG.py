from oneBitClock import oneBitClock
from parcours import ParentTraceur
from parcours import parcours_en_largeur


class semantic2RG:
    def __init__(self,semantic):
        self.semantic=semantic
    
    def root(self):
        return self.semantic.initial()
    
    def neighbors(self, state):
        actions = []
        if not isinstance(state, list):
            state = [state]
        for n in state:
            actions.extend(self.semantic.actions([n]))
        voisins = []
        for action in actions:
            targets = self.semantic.execute(action,state)
            voisins.extend(targets)
        return voisins
        




if __name__ == '__main__':
    clock = oneBitClock()
    print("printing bare obc semantic")
    print(clock.initial())
    for state in clock.initial():
        print(clock.execute(clock.actions([state])[0], [state]))
    
    print("printing obc semantic as a rooted graph using the adaptator")
    adaptator = semantic2RG(clock)
    print('root:')
    print(adaptator.root())
    print('neighbors:')
    print(adaptator.neighbors(adaptator.root()))
    pt = ParentTraceur(adaptator)
    p = parcours_en_largeur(pt, lambda c: c == 1)
    print('states:')
    for state in p:
        print(state)

