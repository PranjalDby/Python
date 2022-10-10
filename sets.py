# Sets is unorderd ,mutable ,no duplicates
from typing import FrozenSet


myset = {1,3,5,7,9}
evens = {2,4,6,8}
primes = {2,3,5,7}
setA = {1,2,3,4,5,6}
setB = {1,2,3}
u = myset.union(evens)
print(u)
# sets method
i = myset.intersection(primes)
diff = myset.difference(primes)
sydiff = myset.symmetric_difference(primes)
print(sydiff)
# print(setB.issubset(setA))
# print(setA.issuperset(setB))
print(setA.isdisjoint(setB))
set3 = setA.copy()
set3.add(55)
print(set3)
print(setA)
# Frozen Sets ar immutable

a = FrozenSet([1,2,3,45])