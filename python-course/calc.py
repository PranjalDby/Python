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

for n in range(6,18+1,3):
    print(n * 2)

for s in range(10):
    print(s* 2)


def cube_recur(num):
    if num == 0:
        return
    print(num ** 3)
    return cube_recur(num-1)

dics = {0:0,1:1}
def fibonnaci(num):
    
    if num in dics:
        return dics[num]
        
    else:
        dics[num] = fibonnaci(num-1) + fibonnaci(num-2)

    return dics[num]



print("recursive cube")
# cube_recur(10)

for i in range(15):
    print(fibonnaci(i))