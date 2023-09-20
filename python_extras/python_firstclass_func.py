# functions a first class object

# function can be passed and used as an arguments

def say_hello(name):
    return f'Hello {name}'

def sout_name(name):
    return f'{name}\n' * 3

def greet_pranjal(greet_func__orsout):
    print(greet_func__orsout('Pranjal'))

greet_pranjal(say_hello)

# function can be defined inside other functions

def math_wrapper(num1):
    def calc_square(num):
        return num ** 2
    
    def calc_cube(num):
        return num ** 3
    

    return calc_cube(num1)

print(math_wrapper(10))

# function can be returned from another function

def func_helper(option):
    def first_func():
        return 'Hello Iam A first Func💕'
    
    def second_func():
        return 'Howdy Iam Second first""s camo 🤣🤣🤣'
    if option == 1:
        return first_func
    
    else: 
        return second_func
    

func = func_helper(9)
print(func())