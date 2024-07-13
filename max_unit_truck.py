# https://leetcode.com/problems/maximum-units-on-a-truck/description/
from typing import List

class Solution:
    def maximumUnits1(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_load = 0
        gen = (x for x in sorted(boxTypes, key=lambda x: x[1], reverse=True))
        while truckSize > 0:
            try:
                boxes, units = gen.__next__()
            except StopIteration as e:
                return total_load
            if truckSize - boxes <= 0:
               total_load += truckSize * units
               return total_load
            else:
                total_load += boxes * units
                truckSize -= boxes
        return total_load

    def maximumUnits2(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_load = 0
        for boxes, units in (x for x in sorted(boxTypes, key=lambda x: x[1], reverse=True)):
            if truckSize - boxes <= 0:
               total_load += truckSize * units
               return total_load
            else:
                total_load += boxes * units
                truckSize -= boxes
        return total_load

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_load = 0
        for boxes, units in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            if truckSize - boxes <= 0:
               total_load += truckSize * units
               return total_load
            else:
                total_load += boxes * units
                truckSize -= boxes
        return total_load



print (Solution().maximumUnits( [[2,10], [1, 5]],  25))
print (Solution().maximumUnits( [[2,10], [2, 5]],  25))
print (Solution().maximumUnits( [[2,10], [1, 5], [2,3]],  26))
print (Solution().maximumUnits( [[2,10], [1, 5], [3,3]],  27))
print (Solution().maximumUnits( [[1,3],[2,2],[3,1]], 4))
print (Solution().maximumUnits( [[5,10],[2,5],[4,7],[3,9]], 10))
