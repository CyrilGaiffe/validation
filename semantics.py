from abc import ABC

class Semantics(ABC):

    def initial(self):
        pass
    
    def actions(self, configuration):
        pass

    def execute(self, actions , c):
        pass



    



