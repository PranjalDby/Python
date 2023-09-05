def add(num1,num2):
    return num1 + num2


def sub(num1,num2):
    return num1 - num2


def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        raise ValueError("Invalid Value detected ex 0")
    
    return num1 / num2