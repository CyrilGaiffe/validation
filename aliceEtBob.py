from semantics import Semantics
from semantics2RG import semantic2RG
from parcours import parcours_en_largeur
from parcours import ParentTraceur

class AliceBob(Semantics):
    def initial(self):
        return ["MaisonAlice","MaisonBob"]

    def actions(self, configuration):
        A = []

        if configuration == ["MaisonAlice"]:
            A.append(lambda c: ["JardinAlice"])
        if configuration == ["JardinAlice"]:
            A.append(lambda c: ["MaisonAlice"])
        if configuration == ["MaisonBob"]:
            A.append(lambda c: ["JardinBob"])
        if configuration == ["JardinBob"]:
            A.append(lambda c: ["MaisonBob"])

        return A
        
    
    def execute(self, action, configuration):
        return action(configuration)
    

if __name__ == '__main__':
    AB = AliceBob()
    adaptator=semantic2RG(AB)
    pt = ParentTraceur(adaptator)
    p = parcours_en_largeur(pt, lambda c: c == ["JardinAlice", "JardinBob"])
    for state in p:
        print(state)