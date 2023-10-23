import timeit


def insertion_sort(arr):
    if arr == None:
        return
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

def selection_sort(array):
    if array == None:
        return
    
    for i in range(len(arr)):
        small = i
        for j in range(i+1,len(arr)):
            if arr[small] > arr[j]:
                small = j
        
        temp = arr[i]
        arr[i] = arr[small]
        arr[small] = temp
            
    return array

def quick_sort(arr,low,high):

    if low <= high:
        pivot = get_pivot(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    
    return


def divide(arr,low,high):

    if low < high:
        mid = (high + low) // 2
        divide(arr,low,mid)
        divide(arr,mid+1,high)
        merge(arr,low,high,mid)

def merge(arr,low,high,mid):
    sorted = []
    for i in range(high-low+1):
        sorted.append(i)
    x = low
    y = mid+1
    z = 0
    while(x<=mid and y <=high):
        if arr[x] < arr[y]:
            sorted[z] = arr[x]
            z+=1
            x+=1
        
        else:
            sorted[z] = arr[y]
            z+=1
            y+=1
    
    while x <= mid:
        sorted[z] = arr[x]
        z+=1
        x+=1

    while y <= high:
        sorted[z] = arr[y]
        z+=1
        y+=1
    for i in range(low,high+1):
        arr[i] = sorted[i-low]

def get_pivot(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp

    return i+1
arr1 = [1,2,4,6,5,3,8,7]


arr = [5,2,4,6,8,1]

# print(insertion_sort(arr))
start = timeit.default_timer()
# high = len(arr)-1
# start1 = timeit.default_timer()
# # arr = selection_sort(arr)
# end1 = timeit.default_timer()

# print("time = ",end1-start1)
# # quick_sort(arr,0,high)
# end = timeit.default_timer()
# print("Total time to execute..",end-start)
# print(arr)
divide(arr,0,len(arr)-1)
print(arr)