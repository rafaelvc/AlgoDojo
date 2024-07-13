# https://leetcode.com/problems/previous-permutation-with-one-swap/
from typing import List
import pdb

class Solution:

    def get_near(self, arr, n):
        if len(arr) < 2:
            return -1
        ix = -1
        dist = None
        for i, v in enumerate(arr):
            if v >= n:
                continue
            if dist is None or abs(v  - n) < dist:
                dist = abs(v - n)
                ix = i
        return ix

    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        minx = min(arr) 
        maxx = max(arr)
        for i in range(len(arr)):
            x = arr[i]
            # if x == minx or x == maxx:
            #    continue
            ix = self.get_near(arr[i+1:], x)
            # pdb.set_trace()
            if ix != -1:
                arr[i], arr[ix+i+1] = arr[ix+i+1], arr[i]
                return arr
        return arr

print (Solution().prevPermOpt1([4,1,5]))
print (Solution().prevPermOpt1([2,1,1]))
print (Solution().prevPermOpt1([1,1,5]))
print (Solution().prevPermOpt1([3,2,1]))
print (Solution().prevPermOpt1([1,9,4,6,7]))