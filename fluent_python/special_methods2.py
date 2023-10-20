import collections

dicts = {1:"pranjal",3:"Dubey",2:"Shyam"}
print(dicts)

class B1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self):
        return self.a + self.b