#https://leetcode.com/problems/merge-sorted-array/

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = (m+n) - 1
    m -= 1
    n -= 1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        elif nums1[m] < nums2[n]:
            nums1[i] = nums2[n]
            n -= 1
        else:
            nums1[i] = nums2[n]
            m -= 1
        i -= 1
    if m == -1 and n >= 0:
        while n >= 0 and i >= 0:
            nums1[i] = nums2[n]
            n -= 1
            i -= 1

nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]
m = n = 3
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1,2,0,0] 
nums2 = [3,4]
m = n = 2
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [3,4,0,0] 
nums2 = [1,2]
m = n = 2
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1,3,0,0] 
nums2 = [2,4]
m = n = 2
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
nums2 = [1]
m = 0
n = 1
merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
nums2 = []
m = 1
n = 0
merge(nums1, m, nums2, n)
print(nums1)