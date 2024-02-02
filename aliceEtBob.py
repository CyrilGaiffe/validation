from semantics import Semantics
from semantics2RG import semantic2RG
from parcours import parcours_en_largeur
from parcours import ParentTraceur

class AliceBob(Semantics):
    def initial(self):
        return [("MaisonAlice","MaisonBob")]

    def actions(self, configuration):
        A = []
        print(configuration)
        if isinstance(configuration, list):
            configuration = configuration[0]

        if configuration[0] == "MaisonAlice":
            A.append(lambda c: [("JardinAlice",configuration[1])])
        if configuration[0] == "JardinAlice":
            A.append(lambda c: [("MaisonAlice",configuration[1])])
        if configuration[1] == "MaisonBob":
            A.append(lambda c: [(configuration[0],"JardinBob")])
        if configuration[1] == "JardinBob":
            A.append(lambda c: [(configuration[0],"MaisonBob")])

        return A
        
    
    def execute(self, action, configuration):
        return action(configuration)
    

if __name__ == '__main__':
    AB = AliceBob()
    adaptator=semantic2RG(AB)
    pt = ParentTraceur(adaptator)
    p = parcours_en_largeur(pt, lambda c: c == ("JardinAlice", "JardinBob"))
    for state in p:
        print(state)