# default arguments

def myfun(x,y=4):
    print(x * y)

myfun(2)

# keyword arguments

def name(first,second):
    print(f'name is {first}{second}')

name(first="Pranjal",second="Dubey")
# variable length arguments
def myfun(*args):
    for arg in args:
        print('.'.join(arg))

def findEven(num):
    '''This Function is to find even or odd'''
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")


myfun("Name","is","Pranjal","Dubey")
print(findEven.__doc__)
# Lamda functions
cube = lambda x: x*x*x
print(cube(3))

# nested functions

def printnme():
    s = "Hello World to "
    def prints():
        print(s)

    prints()

printnme()