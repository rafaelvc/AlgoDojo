
def bin_search1(target, nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + ((r - l) // 2)
        if target == nums[mid]:
            return True
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return False

# print (bin_search1(4,[1,2,3]))
# print (bin_search1(0,[1,2,3]))
# print (bin_search1(0,[1,2,3,4]))
# print (bin_search1(5,[1,2,3,5]))
# print (bin_search1(1,[1,2,3,5]))
# print (bin_search1(3,[1,2,3,5]))
# print (bin_search1(3,[1,2,3,5,6]))
# print (bin_search1(6,[1,2,3,5,6]))
# print (bin_search1(1,[1,2,3,5,6]))
# print (bin_search1(4,[1,2,3,5,6]))
