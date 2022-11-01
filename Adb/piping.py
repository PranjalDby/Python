from logging import FileHandler
import pipe
from pipe import *
import sys
arr = [1,2,3,4,5]
lst = arr|select(lambda x: x*x)
print(list(lst))
file = FileHandler('Pranjal.txt','r')
# filewri = 





