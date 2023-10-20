import collections
import math
from abc import abstractmethod,ABC
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    
class Vector:
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x!r},{self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self,scalar):
        return Vector(self.x * scalar,self.y * scalar)
    
class Abstraction(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def subtract(self,a,b):
        pass

    
class A(Abstraction):
    def __init__(self) -> None:
        super().__init__() 

    def my_sum(self):
        return self.a + self.b
    
    def subtract(self, a, b):
        return a-b
    
a = A()
print(a.subtract(20,6))
deck = FrenchDeck()
print(deck[0])

vector = Vector(2.3,5.4)
vector2 = Vector(3.2,4.3)
print(vector + vector2 )
print(vector * 3)
print(vector == vector)
