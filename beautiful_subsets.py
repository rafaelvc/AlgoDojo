# https://leetcode.com/problems/the-number-of-beautiful-subsets/
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        grp = set(nums)
        # generate all substes
        # total = (2 ** n) - 1
        size_k = 0
        for n in nums:
            if abs(n - k) in grp:
                size_k += 2
            if abs(n + k) in grp:
                size_k += 2
        # return (2 ** (len(nums) - size_k)) - 1
        return (2 ** size_k) - 1
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total = len(nums)
        for i in range(2, len(nums)):
            
        
print (Solution().beautifulSubsets([2,3,4,5], 2))





