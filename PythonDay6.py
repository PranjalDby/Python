from operator import le
from warnings import catch_warnings


matrix = [
[2,5,3,6],
[6,7,10,23],
[10,12,13,15],
[13,56,30,45]
]
#above is 4 x 2 list
# print(matrix[3][1])
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j])

phrase = input("Enter the Phrase ")
translation = ""
for i in phrase:
    if(i.lower() in "aeiou"):
        if(i.isupper()):
            translation = translation + "G"
        else:
            translation = translation + "g"
    else:
        translation = translation + i

print(translation)
'''
very nice thing i see in python is it use in keyword which help me very  much to solve some string based problems
try catch
''' 
try:
    num = 10/0
    number = int(input("Enter the number "))
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Divide by zero")
