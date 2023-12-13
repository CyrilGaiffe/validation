from collections import deque

# class rootedGraph :
#     def __init__(self):
#         pass

#     def roots(self):
#         return self.root
    
#     def neighbors(self, node):
#         return self.graph[node]


def parcours_en_largeur(rootedGraph, query):
    file = deque([rootedGraph.root()])
    visite = set([rootedGraph.root()])
    parents = {}

    while file:
        sommet_courant = file.popleft()

        for voisin in rootedGraph.neighbors(sommet_courant):
            if voisin not in visite:
                file.append(voisin)
                visite.add(voisin)
                if sommet_courant in parents:
                    parents[sommet_courant].append(voisin)
                else :
                    parents[sommet_courant]=[voisin]
                if query(voisin):
                    return (visite,parent(voisin,parents,rootedGraph))
    return visite


def parent(node,dict,rootedGraph):
    result =[]
    courant = node
    while (courant!=rootedGraph.root()):
        result.append(courant)
        for cle,valeur in dict.items():
            for i in range(len(valeur)):
                if valeur[i] == courant:
                    courant = cle
                
    return result
    

# G = rootedGraph({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A')
# print(parcours_en_largeur(G))




class hanoiState:
    def __init__(self, towers):
        self.towers = towers

    def __eq__(self, other):
        return self.towers == other.towers
    
    def __hash__(self):
        return 1


# jeu de hanoï
class hanoiRG:
    def __init__(self):
        pass

    def root(self):
        return hanoiState([[1, 2, 3], [], []])
    
    
    def neighbors(self, state):
        voisins = []

        for source in range(len(state.towers)):
            for target in range(len(state.towers)):
                if source != target:
                    new_state = hanoiState([[], [], []])
                    new_state.towers = [list(tower) for tower in state.towers]
                    if new_state.towers[source]:
                        disk = new_state.towers[source].pop(0)
                        if not new_state.towers[target] or new_state.towers[target][0] > disk:
                            new_state.towers[target].insert(0,disk)
                            
                            voisins.append(new_state)

        return voisins
    
    def isFinalState(self,hanoiState):
        return hanoiState.towers[2] == [1, 2, 3]


h = hanoiRG()
p = parcours_en_largeur(h, h.isFinalState)
for state in p[0]:
    print(state.towers)
print("Solution branch is :\n")
for state in p[1]:
    print(state.towers)
#TODO ajouter la gestion de parents
