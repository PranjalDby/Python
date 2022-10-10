# dict is mutable, unordered , key -value pair

# first way
mydict = dict(name="max",age=23,standard=3)
print(mydict.get("age"))

# second way 
dict2 = {"admin":"rohan","Key":234}
dict2["age"] = 45
print(dict2)
# check key is in our dict 
if "admin" in dict2:
    print("yes")

mydictcpy = dict2.copy()
mydictcpy["admin"] = "singh"
mydict.update(dict2)
print(mydict)
month = {1:"jan",2:"feb",3:"march",4:"April",5:"May",6:"june",7:"july",8:"Aug",9:"sep",10:"oct",11:"nov",12:"dec"}
name = int(input("Enter the month number : "))
print(f'Month is : {month.get(name)}')

mytuple = (8,7)
dicts = {mytuple:15}
print(dicts.get(mytuple))