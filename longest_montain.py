# https://leetcode.com/problems/longest-mountain-in-array/
from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        big_mountain = 0
        for i in range(1,len(arr)-1):
            left, right = i-1, i+1
            if arr[left] < arr[i] and arr[right] < arr[i]: # Found a mointain, check size
                mountain_size = 3
                left -= 1
                right += 1
                increase = True
                while increase:
                    increase = False
                    if left >= 0 and arr[left] < arr[left+1]:
                        mountain_size += 1
                        left -= 1
                        increase = True
                    if right < len(arr) and arr[right] < arr[right-1]:
                        mountain_size += 1
                        right += 1
                        increase = True
                big_mountain = max(mountain_size, big_mountain)
        return big_mountain

print (Solution().longestMountain( [2,1,4,7,3,2,5] ))
print (Solution().longestMountain( [2,2,2] ))
print (Solution().longestMountain( list ( range(3) ) + [0] ))
print (Solution().longestMountain( [0,1,2,3,4,5,4,3,2,1,0] ))
print (Solution().longestMountain( [0,1,2,3,4,5,6,7,8,9] ))
print (Solution().longestMountain( list(range(5)) + [0] ))
