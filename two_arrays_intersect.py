# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List

# O(M+N)
def two_array_intersect( arr1, arr2 ):

    # counter_dict = {}
    
    # # for i in arr1:
    # #     if counter_dict.get(i):
    # #         counter_dict[i] += 1
    # #     else:
    # #         counter_dict[i] = 1

    # for i in arr1: 
    #     counter_dict[i] = counter_dict.get(i, 0) + 1 
    # # result = []
    # result = set()
    # for j in arr2:
    #     if j not in result and counter_dict.get(j):
    #         # counter_dict[j] -= 1
    #         result.add( j )
    #         # result.append( j )

    result = set()
    # set1, arr = set( arr1 ), arr2 if len(arr1) < len(arr2) else set( arr2 ), arr1    
    set1 = set( arr1 ) if len(arr1) < len(arr2) else set( arr2 )
    arr =  arr1 if len(arr1) > len(arr2) else arr2 
    # map( lambda x: result.add(x) if x in set1 else [], arr) 
    return  list(set(list(filter(lambda x: x if x in set1 else [], arr) )) )
    # for j in arr: 
    #     if j in set1:
    #         result.add(j)
    # result = list(result)
    # return result

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if max(nums1) < min (nums2) or\
           max(nums2) < min (nums1):
                return []
            
        counter_dict = {}
        
        if len(nums1) > len(nums2):
            arr2, arr1 = nums1, nums2
        else:
            arr1, arr2 = nums1, nums2
    
        # for i in arr1:
        #     if counter_dict.get(i):
        #         counter_dict[i] += 1
        #     else:
        #         counter_dict[i] = 1

        for i in arr1: 
            counter_dict[i] = counter_dict.get(i, 0) + 1 

        result = []
        for j in arr2:
            if counter_dict.get(j):
                counter_dict[j] -= 1
                result.append( j )

        return result


arr1, arr2 = [1,2,1], [2,2]
print (two_array_intersect(arr1, arr2) )

arr1, arr2 = [4,9,5], [9,4,9,8,4]
print (two_array_intersect(arr1, arr2) )