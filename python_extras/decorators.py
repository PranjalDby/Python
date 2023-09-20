from datetime import datetime
import functools
import math
from decorators_utils import *
import time
def my_decorator(func):
    def wrapper():
        print('Hello first statement b')
        func()
        print('After Something happend..finally i got the time..')

    return wrapper

def not_night(func):

    def wrapper(*args,**kwargs):
        if 7 <= datetime.now().hour < 22:
            print('you have the permission to say whee')
            func(*args,**kwargs)
        else:
            return 'Hush.....neighbours is sleeping'
        
    return wrapper

# decoration is happening at this line -13
# using decorators by using @ pie symbol

# passing an arguments to the decorated function
@not_night
@do_twice
def say_whee(name,title):
    print(f'{name} >> life is like a bamboo growing very fast and now i have to say  whee...huh...wheeeee')
    print(f'your title is = {title}')



# returning value from decorator

def calc_cube(num):
    return num ** 3

def math_wrapper(func):
    #we use this module to preserve the original information of our function
    @functools.wraps(func)
    def wrapper(*args):
        print('solving problem..')
        return func(*args)
    return wrapper

@math_wrapper
def calc_square(num):
    sqr = []
    for i in num:
        sqr.append(i ** 2)

    return sqr


sq = calc_square([10,11])
print(sq)
@timer
def iter():
    for __ in range(100):
        value = sum([i ** 2 for i in range(10000)])

    print("value = ",value)

print(iter())
@debugging
def greeting(name,age=None):
    if age is None:
        return f"Howdy {name}!"
    
    else:
        return f"Whoa {name}! {age} already, you are growing up"
    

def approximate_e(terms=18):
    return sum(1/math.factorial(n) for n in range(terms))
