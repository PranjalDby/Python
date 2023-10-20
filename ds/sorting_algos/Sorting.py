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
arr = [1,2,4,6,5,3,8,7]

start1 = timeit.default_timer()
arr = selection_sort(arr)
end1 = timeit.default_timer()
print("total time taken by selection sort",end1-start1)

arr = [5,2,4,6,1,3,8,7,11,14]

# print(insertion_sort(arr))
start = timeit.default_timer()
high = len(arr)-1
quick_sort(arr,0,high)
end = timeit.default_timer()
print("Total time to execute..",end-start)
print(arr)