"""
Position: Senior Py dev.

For a list of n planks and its variable length n(i) return the highest fence (number of planks) 
where all planks have same size. It is possible to use two planks to build up a new plank.

Example: For [10,10,10,3,4,10], result = 4, A fence with 4 planks of length 10. 3+4 can't form a 10 length plank.
             [10,10,10,5,5,10], result = 5. A fence with 4 planks plus one (5+5)
           
"""

from collections import Counter
from itertools import combinations

""" 
The idea was to first account number of most common planks of same size, 
then pin point remaining combination of pairs of planks where sum of them equals to 
most common length.  (This algo was only 44%)
"""

"""
In my original solution I missed a way of remove or mark 
used planks and disconsider pairs of planks were already used.
"""

def max_fence_size(planks_list):
    most_common = Counter(planks_list).most_common()
    most_common, counter = most_common[0]
    used_planks = set()
    for a in range(0, len(planks_list)): 
        if planks_list[a] >= most_common:
            continue
        for b in range(a+1, len(planks_list)):
            if planks_list[b] >= most_common:
                continue
            if a not in used_planks and b not in used_planks\
                and (planks_list[a]+planks_list[b]) == most_common:
                used_planks.add(a)
                used_planks.add(b)
                counter += 1
    return counter

print (max_fence_size([10,10,10,3,4,10]))
print (max_fence_size([10,10,10,5,5,10]))
print (max_fence_size([2,2,1,1,1,10]))
print (max_fence_size([2,2,1,1,1,2,10]))








