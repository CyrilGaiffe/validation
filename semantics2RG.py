from oneBitClock import oneBitClock
from parcours import ParentTraceur


class semantic2RG:
    def __init__(self,semantic):
        self.semantic=semantic
    
    def root(self):
        return self.semantic.initial()
    
    def neighbors(self, state):
        actions = []
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
    print(adaptator.root())
    print(adaptator.neighbors(adaptator.root()))
    pt = ParentTraceur(adaptator)

