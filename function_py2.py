num1 = int(input("enter the first num: "))
num2 = int(input("enter the first num: "))
option = input("enter the operation + - * ")
if(option == "+"):
    sum = num1 + num2
elif(option == "-"):
    print("num1 - num 2 = ",num1 - num2)
elif(option == "*"):
    print("num1 * num2 = ",num1 * num2)
else:
    print("OOPS!! wrong operator")

"""
Dictionary in python is key:value pair
it look like a hash map
"""
dict = {
    #key : value
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}
print(dict.get("Jan") + dict["Mar"])
