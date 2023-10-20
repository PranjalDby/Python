# memory views
from array import array

octet = array('b',range(6))

# memoryview is like a numpy but without the math
m1 = memoryview(octet)
print(m1.tolist())
m2 = m1.cast('b',(2,3))
print(m2[0,1])
print(m2.tolist()[0])
print(m2.tolist())
numbers = array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
memv_oct[4] = 5
print(memv_oct.tolist())
print(numbers)