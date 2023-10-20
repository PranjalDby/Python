# pep 695 type parameter syntax
import dis
from pyparsing import Iterable
def sum_generic[T](args:Iterable[T]) ->T:
    s:[T] = args[0]
    print(type(s))
    for i in args:
        s = s + i

    return s

sums = sum_generic([1,2,3,4,5,6,7,8])
print(sums)
print('more powerful f-string')

from datetime import date
from collections.abc import Sequence
major = 3
minor = 11
release = date(2023,10,2)
print(f"Python {major}.{minor+1} is released on {release:%b-%d}")
print('nested formatted string...')
print(f"most-outer{f" 1-inner{f" most-inner "}out-1 "}most-out")
version  = {"major":3,'minor':12}
print(f"Version = {version["major"]}.{version['minor']}")

# using backslash inside f-string
names = ["Brett",'Emily','gregory','pablo']

print(f'steering councel:\n{"\n".join(names)}')
# inline comprehensions
# res = [name[::-1].title() for name in names]

def reverse_name(names):
    return [name[::-1].title() for name in names]

print(reverse_name(names))
dis.dis(reverse_name)

# dedicated type variable syntax

# using type variable

# its a generic functions parametrized by type variable 'T'
# we help our interpreter by defining the type explicitly
def first[T](elements:Sequence[T]) -> T:
    return elements[0]

print(first([1,2,4,]))

#constrained
# freed
# bounded

def free[T](argument:T) -> T:
    print(f'this {argument} can be subtype of any type..')

# it be a subtype of few types defined explicitly
def constrained[T:(int,float,complex)](argument:T) ->T:
    print(f'this {argument} can be any subtype that is int,float and complex number..')

# it can be bounded as a subtype of some type

def bounded[T:str](arg:T) -> T:
    pass


# generic classes

class Stack[T]:
    def __init__(self):
        self.stack:list[T] = []

    def push(self,data):
        self.stack.append(data)

    def pop(self,data):
        self.stack.pop()

    def __repr__(self) -> str:
        return "hey .. i mean yay"

stk = Stack[int]()

stk.push(30)
stk.push(50)
stk.push(40)
stk.push(20)
print(stk)