# Tuples ordered ,immutable,allows duplicate
import sys
# mytuple = ("Max",28,"begonia")
# second way
mytuple  = ("begonia",)
#third way
my = tuple(["max",45,"newyork"])
# convertin tuple to lists
lists = list(my)
print(lists)

num = (1,2,3,4,5,6,7)
numlist = [1,2,3,4,5,6,7]
b = num[::-1]
print(b)
# unpacking
# first way
name,age,city = my
print(name,age,city)
# second way 
i1,*i2,i3= num
print(i1,i2,i3)
# tuple is efficient than list
print(sys.getsizeof(num),"bytes")
print(sys.getsizeof(numlist),"bytes")