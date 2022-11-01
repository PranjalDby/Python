
import functools
import math
import time

def create_ad(x):
    def adder(y):
        return x+y
    return adder

add15 = create_ad(15)

print(add15(10))

def decorator(func):
    def inner(*args,**kwargs):
        print('Hello inner')
        func(*args,**kwargs)
        print('end')
    return inner 

def functi(times):
    print(('hi ' + '') * times)

@decorator
def print_greeting_with_name(name):
    print(name)

# functi = decorator(functi)
# times = 7
# functi(7)

def calculate_time(func):
    def inner(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('Time taken to execute: ' ,func.__name__,end-begin)

    return inner
@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

# factorial(5)
# print_greeting_with_name('Pranjal')
'''
functions with return value
'''
def summation(func):
    @functools.wraps(func)
    def adder(*args,**kwargs):
        print('adding two nums.. ')
        res = func(*args,**kwargs)
        return res
    return adder
        
def design(func):
    def wrap(*args,**kwargs):
        print("*********************")
        res = func(*args,**kwargs)
        if(res != None):
            print(res)
        print('@@@@@@@@@@@@@@@@@@@@@@@@')
    return wrap

@summation
@design
def sum(num,num2):
    print(num + num2)

sum(10,40)

# class decorators

class Home:
    def __init__(self,func):
        self.time = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.time += 1
        print(f"No of time Executed: {self.time}")
        return self.func(*args,**kwargs)

@Home
@calculate_time
def printfun(name):
    print(f'hello {name}')

printfun('pranjal')
printfun('pranjal')
printfun('pranjal')
printfun('pranjal')
printfun('pranjal')






