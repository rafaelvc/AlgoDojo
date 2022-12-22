# https://leetcode.com/problems/search-insert-position/

# Binary search
def search_insert(nums, target):
    if target > nums[len(nums)-1]:
        return len(nums)
    elif target < nums[0]:
        return 0
    l = 0
    r = len(nums) - 1
    mid = r // 2
    while l <= r:
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
            mid = l + ((r - l) // 2)
        else:
            r = mid - 1
            mid = r // 2
    if target > nums[r]:
        return r+1
    return l-1

print (search_insert(nums = [1,3,5,6], target = 5))
print (search_insert(nums = [1,3,5,6], target = 2))
print (search_insert(nums = [1,3,5,6], target = 7))
print (search_insert(nums = [1,3,5,6], target = 6))
print (search_insert(nums = [1,3,5,6], target = 3))
print (search_insert(nums = [1,3,5,6,8], target = 1))
print (search_insert(nums = [1,3,5,6,8], target = 8))
print (search_insert(nums = [1,3,5,7,8], target = 6))