from collections import deque
from abc import ABC

class rootedGraph(ABC) :
    def __init__(self):
        pass

    def roots(self):
        return self.root
    
    def neighbors(self, node):
        return self.graph[node]


def parcours_en_largeur(rootedGraph, query):
    file = deque([rootedGraph.root()])
    visite = set([rootedGraph.root()])

    while file:
        sommet_courant = file.popleft()

        for voisin in rootedGraph.neighbors(sommet_courant):
            if voisin not in visite:
                file.append(voisin)
                visite.add(voisin)
                if query(voisin):
                    return visite
    return visite
    

# G = rootedGraph({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A')
# print(parcours_en_largeur(G))




class hanoiConfiguration:
    def __init__(self, towers):
        self.towers = towers

    def __eq__(self, other):
        return self.towers == other.towers
    
    def __hash__(self):
        return 1


# jeu de hanoï
class hanoiRG(rootedGraph):
    def __init__(self, root = hanoiConfiguration([[1, 2, 3], [], []])):
        self.racine = root

    def root(self):
        return self.racine
    
    
    def neighbors(self, state):
        voisins = []

        for source in range(len(state.towers)):
            for target in range(len(state.towers)):
                if source != target:
                    new_state = hanoiConfiguration([[], [], []])
                    new_state.towers = [list(tower) for tower in state.towers]
                    if new_state.towers[source]:
                        disk = new_state.towers[source].pop(0)
                        if not new_state.towers[target] or new_state.towers[target][0] > disk:
                            new_state.towers[target].insert(0,disk)
                            
                            voisins.append(new_state)

        return voisins
    
    def etatFinal(self,hanoiState):
        return hanoiState.towers[2] == [1, 2, 3]
    


class ParentTraceur(rootedGraph):

    def __init__(self, rootedGraph):
        self.graphe = rootedGraph
        self.parents={}

    def root(self):
        root = self.graphe.root()
        for state in root:
            self.parents[state]=[]
        return root
    
    def neighbors(self, state):
        voisins = self.graphe.neighbors(state)
        for voisin_state in voisins:
            if voisin_state not in self.parents:
                self.parents[voisin_state]=[state]
            else : 
                self.parents[voisin_state].append(state)
        return voisins
    
    def trace(self):
        noeud = next(k for k,v in self.parents.items if self.graphe.etatFinal(k))
        trace = [noeud]
        while noeud not in self.root :
            parent = self.parents[noeud][0]
            trace.insert(0,parent)
        return trace



h = hanoiRG()
p = parcours_en_largeur(h, h.etatFinal)
for state in p:
    print(state.towers)
