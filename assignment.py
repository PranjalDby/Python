val = int (input("Enter The  first Number: "))
val2 = int (input("Enter The  second Number: "))

if(val % 2 == 0 and val2 %2 == 0):
    print(f"{val} and {val2} is even")
else:
    if val % 2 == 0 or val2 % 2 !=0:
        print(f"{val} is even and {val2} is odd")
    else:
        print(f"{val} is odd and {val2} is even")