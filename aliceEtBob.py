from semantics import Semantics

class AliceBob(Semantics):
    def initial(self):
        return ["Alice","","Bob"]

    def actions(self, configuration):
        A=[]
        if configuration[1] == "":
            #no one is in the garden
            A.append(lambda c : [c[1],c[0],c[2]])
            A.append(lambda c : [c[0],c[2],c[1]])

        else :
            if configuration[2] == "":
               #Bob is in the garden
                A.append(lambda c : [c[0],c[2],c[1]])
            else:
                A.append(lambda c : [c[1],c[0],c[2]])
        return A
    
    def execute(self, action, configuration):
        return action(configuration)
