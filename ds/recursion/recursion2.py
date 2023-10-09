import numpy as np
def sum_of_natural(num):
    if num == 0 :
        return 0
    
    else:
        return num +  sum_of_natural(num-1)
    
print(sum_of_natural(10))

def binary_search(arr,start,stop,find):
    if start > stop:
        return -1
    
    mid = (start+stop) // 2
    if find == arr[mid]:
        return mid
    
    if find < arr[mid]:
        return binary_search(arr,start,mid-1,find)
    
    return binary_search(arr,mid+1,stop,find)

# given array must be sorted

arr = [1,6,8,10,12,15]
print(binary_search(arr,0,len(arr)-1,12)) 
#space complexity O(1) and time complexity O(n * logn)

print("Fibonacci series")

def fibonacci(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
# print(fibonacci(8 ))
def divide(arr,start,end):
    if start < end:
        mid = (start+end) // 2
        divide(arr,start,mid)
        divide(arr,mid+1,end)
        merge(arr,start,mid,end)

def merge(arr,start,mid,end):
    temp = np.zeros(shape=(end-start+1,),dtype=int)
    x = start
    y = mid+1
    k = 0
    while x <= mid and y <= end:
        if arr[x] < arr[y]:
            temp[k] = arr[x]
            k+=1
            x+=1
        else:
            temp[k] = arr[y]
            k+=1
            y+=1

# if right sub array run out of values
    while x <= mid:
        temp[k] = arr[x]
        k+=1
        x+=1
    # if left sub array run out of values
    while y <= end:
        temp[k] = arr[y]
        k+=1
        y+=1

    for i in temp:
        print(i,end=" ")
    for i in range(start,end+1):
        arr[i] = temp[i-start]

    

unsorted = [1,-1,0,6,2,8,7,11]
divide(unsorted,0,len(unsorted)-1)
print(unsorted)
