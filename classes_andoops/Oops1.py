class Car:
    name=""
    color=""
    def __init__(self,name,color):
        self.name = name;
        self.color = color;

'''
1.inheritance
2.abstraction
3.polymorphism
4.encapsulation
'''

class Honda(Car):
    price=0
    isavailable=""
    def __init__(self, name, color,price,isavailable):
        super().__init__(name, color)
        self.price = price
        self.isavailable = isavailable

    def getInfo(self):
        print(f'is avi = {self.isavailable} and price = {self.price}')

class Bird:
    def canotfly(self):
        print("Not all Bird can fly")
    
    def canfly(self):
        print("some bird's can fly")

class Sparrow(Bird):
    def canfly(self):
        print('Sparrow can fly')
    


honda = Honda("Honda",'red',10000,True)
honda.getInfo()
sp = Sparrow()
sp.canfly()