# it is also called dunder
import inspect
from queue import Queue as q
from tokenize import String


class Person:
    def __init__(self,name):
        self.name = name

# dunder method
    def __repr__(self) -> str:
        return self.name

    def __mul__(self,x):
        self.name = self.name * x

        return self.name

    def __call__(self,y):
        print(y)


class Queue(q):
    def __repr__(self) -> str:
        return f"Queue({self._qsize()})"

    def __add__(self,item):
        self.put(item)

q = Queue()
q+3
q+9
print(q)