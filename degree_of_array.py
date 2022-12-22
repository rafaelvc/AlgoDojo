# https://leetcode.com/problems/degree-of-an-array/
import math

def smallest_contiguos(arr):
    array_size = {}
    elemens = []
    degree = 0
    for i,e in enumerate(arr):
        if e in array_size:
            min_ix, max_ix, freq = array_size[e]
        else:
            min_ix, max_ix, freq = i, None, 0
        max_ix = i
        freq += 1
        array_size[e] = min_ix, max_ix, freq
        if freq > degree:
            elemens = [e]
            degree = freq
        elif freq == degree:
            elemens.append(e)
            degree = freq
    smallest = math.inf
    for e in elemens:
        min_ix, max_ix, freq = array_size[e]
        smallest = min(smallest, (max_ix - min_ix)+1)
    return smallest

arr = [1,2,2,3,1]
print (smallest_contiguos(arr))

arr = [1,2,2,3,1,4,2]
print (smallest_contiguos(arr))