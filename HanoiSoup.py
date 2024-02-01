from Soup import *
from semantics2RG import *
from parcours import *

class HanoiSoupConfig(SoupConfiguration):
    def __init__(self,n):
        self.towers=[[1,2,3],[],[]] 

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.towers == other.towers
    
    def __str__(self):
        return "towers "+str(self.towers)
    
    def actionMoveDisk(self,source, destination):
        self.towers[destination].append(self.towers[source].pop()) 

    def etatFinal(self):
        return self.towers[2] == [1, 2, 3]

    

if __name__=='main':
    def hanoiAction(objet, source, destination):
        return objet.actionMoveDisk(source, destination)

    def hanoiGarde(objet, source, destination):
        return objet.towers[source] and objet.towers[source][0] > objet.towers[destination][0]
    
    initial = HanoiSoupConfig()
    pieces = [Piece("moveDisk", hanoiGarde, hanoiAction)]
    soupe = SoupSpec(initial, pieces)
    soupeSemantics = SoupSemantics(soupe)
    adaptator = semantic2RG(soupeSemantics)
    print(adaptator.root())
    print(adaptator.neighbors(adaptator.root()))