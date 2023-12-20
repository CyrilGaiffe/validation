import semantics
import random

class oneBitClock(semantics):
    def initial(self):
        return [random.choice([0,1])]
    
    def actions(self, c):
        A=[]
        if(c==[1]):
            A.append(lambda c : [0])
        else:
            A.append(lambda c : [1])
        
    
    def execute(self, a , c ):
        listConfig = []
        for action in a:
            listConfig.append(a(c))
