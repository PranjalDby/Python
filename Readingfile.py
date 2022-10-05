from io import UnsupportedOperation
from os import read
try:
    count = 0
    empfile = open("emp.txt","a")
    val = input("Enter the text ")

    empfile.write("\n" + val)
    val2 = val
    empfile.close()
except FileNotFoundError:
    print("File Not Found")
except UnsupportedOperation:
    print("Created")

