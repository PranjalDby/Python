# decorating class means decorating the property and methods defines inside the class
"""
some builtins class methods
@classmethod,@property,@static method
"""

import math
from decorators_utils import *
@singleton
class Circle:
    def __init__(self,radius):
        self.rad = radius

    @property
    def radius(self):
        return self.rad
    
    @radius.setter
    def radius(self,value):
        if value >= 0:
            self.rad = value
        else:
            raise ValueError("-ve value")
        

    @property
    def area(self):
        return self.pi() * self.rad ** 2
    
    @classmethod
    def unit_circle(cls):
        return cls(1)
    
    @staticmethod
    def pi():
        return math.pi
    
# c = Circle(34)
# print(c.area)

c1 = Circle(22)
print(c1.area)
# decorating class

@timer
class TimeWaster:
    def __init__(self,max_num):
        self.max_num = max_num

    def waste_time(self,num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])



def cache(func):
    def wrapper_cache(*args,**kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args,**kwargs)
        
        return wrapper_cache.cache[cache_key]
    
    wrapper_cache.cache = dict()
    return wrapper_cache

@count_calls
@cache
def fibonnaci(num):
    if num < 2:
        return num
    
    return fibonnaci(num-1) + fibonnaci(num-2)
@count_calls
@repeat(n_times=10)
def greet(name):
    print(f"hello {name}")
    print(greet.extras)


print("fib",fibonnaci(10))

