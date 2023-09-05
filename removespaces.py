def remove(str):
    list = []
    for i in range(len(str)):
        if(str[i]!=' '):
            list.append(str[i])
    return toString(list)
    

def toString(list):
    str = ''.join(list)
    return str.strip()

str = str(input("Enter the string: "))
print(remove(str))

