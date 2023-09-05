'''
Metaclasses are used to define the rules for class
'''
from MetaclassHelp import *
# class Test:
# #     pass
# class Foo:
#     def show(self):
#         print('hi')

#     def add(self):
#         self.z = 9

# # second Way
# Test = type('Test',(Foo,),{"x":5,"add":Foo.add})
# t = Test()
# t.wy = 'Heloo'
# print(t.wy)
# t.add()
# t.show()
# print(t.z)
class Dog(metaclass=Meta):
    x= 5;
    y = 8;
    
    def hello(self):
        print('hi')