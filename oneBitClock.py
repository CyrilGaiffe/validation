from semantics import Semantics

class oneBitClock(Semantics):
    def initial(self):
        return [0,1]
    
    def actions(self, c):
        A=[]
        if(c==[1]):
            A.append(lambda c : [0])
        else:
            A.append(lambda c : [1])
        
    
    def execute(self, a , c ):
        return a(c)
