from parcours import parcours_en_largeur

class Person :
    def __init__(self, name):
        self.name = name

class GardenConfiguration:
    def __init__(self,garden):
        self.garden = garden

    def __eq__(self, other):
        return self.garden == other.garden
    
    def __hash__(self):
        return 1


class Garden:
    def __init__(self, root = GardenConfiguration([Person("Alice"),0,Person("Bob")])):
        self.racine = root

    def root(self):
        return self.racine
    
    def neighbors(self, state):
        voisins = []
        if state.garden[1] == 0:
            voisins.append(GardenConfiguration([Person("Alice"), Person("Bob"), 0]))
            voisins.append(GardenConfiguration([0, Person("Alice"), Person("Bob")]))
        else :
            voisins.append(GardenConfiguration([Person("Alice"), 0, Person("Bob")]))

        return voisins
