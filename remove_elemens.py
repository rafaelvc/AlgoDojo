# https://leetcode.com/problems/remove-element/

def remove_elemen(arr, val):
    l, r, remain = 0, len(arr)-1,len(arr)
    while l <= r:
        if arr[l] == val:
            if arr[r] != val:
                arr[l] = arr[r]
                l += 1
            r -= 1
            remain -= 1
        else:
            l += 1
    return remain

nums, val = [3,2,2,3], 3
print (remove_elemen(nums, val), nums)

nums, val = [0,1,2,2,3,0,4,2], 2
print (remove_elemen(nums, val), nums)

nums, val = [], 0
print (remove_elemen(nums, val), nums)

nums, val = [3,3,3,3], 3
print (remove_elemen(nums, val), nums)
 
nums, val = [4,5], 4 
print (remove_elemen(nums, val), nums)