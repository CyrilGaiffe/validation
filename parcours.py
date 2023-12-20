from collections import deque
from abc import ABC

#TODO : faire des fichiers propres séparés
#TODO : gérer prorement les listes de root
#TODO : bosser sur alice et Bob pour vérifier dans un premier temps qu'ils arrivent tous les deux dans le jardin puis mettre les flags et ainsi de suite

class RootedGraph(ABC) :
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




class HanoiConfiguration:
    def __init__(self, towers):
        self.towers = towers

    def __eq__(self, other):
        return self.towers == other.towers
    
    def __hash__(self):
        return 1


# jeu de hanoï
class HanoiRG(RootedGraph):
    def __init__(self, root = HanoiConfiguration([[1, 2, 3], [], []])):
        self.racine = root

    def root(self):
        return self.racine
    
    
    def neighbors(self, state):
        voisins = []

        for source in range(len(state.towers)):
            for target in range(len(state.towers)):
                if source != target:
                    new_state = HanoiConfiguration([[], [], []])
                    new_state.towers = [list(tower) for tower in state.towers]
                    if new_state.towers[source]:
                        disk = new_state.towers[source].pop(0)
                        if not new_state.towers[target] or new_state.towers[target][0] > disk:
                            new_state.towers[target].insert(0,disk)
                            
                            voisins.append(new_state)

        return voisins
    
    def etatFinal(self,hanoiState):
        return hanoiState.towers[2] == [1, 2, 3]
    


class ParentTraceur(RootedGraph):

    def __init__(self, rootedGraph):
        self.graphe = rootedGraph
        self.parents={}

    def root(self):
        root = self.graphe.root()
        self.parents[root]=[]
        return root
    
    def neighbors(self, state):
        voisins = self.graphe.neighbors(state)
        for voisin_state in voisins:
            if voisin_state not in self.parents:
                self.parents[voisin_state]=[state]
        return voisins
    
    def trace(self):
        trace=[]
        #partir de l'état final, remonter jsuqu'à la racine
        systeme = parcours_en_largeur(self, self.graphe.etatFinal)
        solution = None
        for noeud in systeme:
            if self.graphe.etatFinal(noeud):
                solution = noeud 
                break
        trace.append(solution)
        while solution != self.graphe.root():
            solution = self.parents[solution][0]
            trace.append(solution)
        return trace



h = HanoiRG()
pt=ParentTraceur(h)
# p = parcours_en_largeur(h, h.etatFinal)
# for state in p:
#     print(state.towers)
# for state in pt.trace():
#     print(state.towers)
