'''
Function in python
flow controle of Program is top to bottom
'''
from operator import le


arr = [4,5,6,7]
#      0 1 2 3
size = len(arr)
def func():
    print("Hello")
    print("There")

def sum(a , b):
    return a+b

def age(age):
    if(age<18):
        return "Not Possible"
    else:
        return "Possible"  

def insert_last(num,siz):
    count=0
    for i in range(0,siz-1):
        count=i+1
    arr[count]=num
arr = [4,5,6,7]
#      0 1 2 3      
func()
print(type(sum(7,8)))
print("is possible " + age(90))

is_male = True 
is_tall = False
if is_male and is_tall:
    print("Congrats! you are male or tall or both ") 
elif is_male and not(is_tall):
    print("You are short male")
else:
    print("ummm you are Female or TransGender")    


