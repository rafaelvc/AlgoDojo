# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
# incorrect solutions needs review
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        ones = 0
        circular_size = 0
        l = 0
        r = len(nums)-1
        while l < r and (nums[l] or nums[r]):
            if nums[l]:
                circular_size += 1
                l += 1
                ones += 1
            if nums[r]:
                circular_size += 1
                r -= 1
                ones += 1
        if len(nums) % 2 > 0 and nums[l]:
            circular_size += 1
        subarr_big = 0
        j = 0
        while (l < r):
            if nums[l]:
                sizes = 0
                j += 1
                while nums[l] and l < r:
                    l += 1
                    sizes += 1
                    ones += 1
                subarr_big = max(subarr_big, sizes)
            else:
                l += 1
        # if circular_size == 0 and len(sizes) == 2:
        #    return 0
        # return 0 if circular_size == 0 and len(sizes) == 2 else ones - max(circular_size, subarr_big)
        return ones - max(circular_size, subarr_big)
            
# print (Solution().minSwaps([1,1,1,0,0,1,0,1,1,0]))
# print (Solution().minSwaps([1,1,1,0,1,1,0,1,1,0,0]))
print (Solution().minSwaps([0,1,1,0]))
print (Solution().minSwaps([0,1,0,1,1,0,0]))
print (Solution().minSwaps([0,1,1,1,0,0,1,1,0]))
print (Solution().minSwaps([1,1,0,0,1]))
