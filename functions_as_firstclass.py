import math
'''
H!>Functions as a first class member......
1)we can pass functions as a parameter to other functions
2)we can return function from function
3)we can store a functions in a variable
4)functions is an instance of a object
5)we can store functions in data structures ex dict,list sets..
'''
# 1)
def calcSqr(check):
    num = check
    return num * num

def check(num):
    if(num < 0):
        return 0
    else:
        return num

print(calcSqr(check(5)))

# 2)
list = [1,2,3,4,5,6,7]
def getCube(list): 
    def returnCube(list):
        num = [];
        for i in range(len(list)):
            cube = int(math.pow(i,3))
            num.append(cube)
        return num
    return returnCube(list)
    

# 4)
def convertUpper(str):
    return str.upper()

upp = convertUpper
print(upp("pranjal"))




