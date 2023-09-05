
from array import array
from time import time
from timeit import default_timer as timer
from typing import List
# my_str = """Pranjal's rom\
#     twitch is Best Platform \
        
# """
my_str = ['a'] * 100000
start = timer()
myst =" "
for i in my_str:
    myst+=i
stop = timer()
print(stop-start)

start =timer()
myst = ''.join(my_str)
stop = timer()
print(stop - start)

# formating string
# by using %
var = 3.44
# mysts= "this is %.2f" %var
# by using {} 
# mysts= "this is {:.2f}".format(var)
# newest way f''
mysts= f'this is {var * 2}'
print(mysts)

