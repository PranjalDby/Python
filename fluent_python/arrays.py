from array import array
from random import random

floats = array('d',(random() for i in range(10 ** 5)))
print(floats[-1])

with open('floats.bin','wb') as file:
    floats.tofile(file)