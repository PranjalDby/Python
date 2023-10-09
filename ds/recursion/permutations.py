nums = [1,2,3]
# to return all the possible permutations from a given array
# [1,2,3],[3,2,1],[2,1,3],[1,3,2],[2,3,1],[3,1,2]
def helper(nums,curr,new_arr):
    result = []
    result =  permutation(nums,curr,new_arr)
    return result
def permutation(nums,new_arr,curr):
    if not len(nums) and len(curr):
        new_arr.append(curr)
        return new_arr
    else:
        for i in range(len(nums)):
            newArr = nums[:i] + nums[i+1:]
            print("Value of NewArr is {} at i = {}".format(newArr,i),end="\n")
            newCurr = curr + [nums[i]]
            print("Value of curr is {} at i = {}".format(newCurr,i),end="\n")
            permutation(newArr,new_arr,newCurr)
        return new_arr

print(helper(nums,[],[]))
li = [1,2,3,4,5,6,7,8]
print(li[1:])