from cProfile import Profile
from pstats import SortKey, Stats
import random as r
from bin_search_check import bin_search1

# Cracking code interview - pag. 67. Bottleneck

def numbers_diff_k_brute_force(arr, k):
    # result = []
    # for ix, n in enumerate(arr):
    #     for m in range(ix+1, len(arr)):
    #         # if (n < arr[m] and n + k == arr[m]) or arr[m] + k == n:
    #         if abs(arr[m]-n) == k:
    #           result.append( tuple(sorted((n, arr[m]))) )
    # return result
    # return [(n, arr[m]) for ix, n in enumerate(arr) for m in range(ix+1, len(arr)) if (n < arr[m] and n + k == arr[m]) or arr[m] + k == n]
    # return [tuple(sorted((n, arr[m]))) for ix, n in enumerate(arr) for m in range(ix+1, len(arr)) if (n < arr[m] and n + k == arr[m]) or arr[m] + k == n]
    return [tuple(sorted((n, arr[m]))) for ix, n in enumerate(arr) for m in range(ix+1, len(arr)) if abs(arr[m]-n) == k]

def numbers_diff_k_hash(arr, k):
    # hash_tb = {n : ix for ix, n in enumerate(arr)}
    arr_set = set ( arr )
    return [tuple(sorted( (n, m) )) for n, m in map(lambda n: (n, n + k), arr) if m in arr_set]

def numbers_diff_k_sorted(arr, k):
    arr = sorted( arr )
    return [(n, m) for n, m in map(lambda n: (n, n + k), arr) if bin_search1(m, arr)]  
    
# # print (numbers_diff_k_brute_force([1,7,5,9,2,12,3], 2))
# # print (numbers_diff_k([1,7,5,9,2,12,3], 2))
nums = [ r.randrange(20) for n in range(1000000) ]
with Profile() as profile:
#    print(f"{numbers_diff_k(nums, 2)}")
    x = numbers_diff_k_hash(nums, 2)
    (
      Stats(profile)
      .strip_dirs()
      .sort_stats(SortKey.CALLS)
      .print_stats()
    )
with Profile() as profile:
    # print(f"{numbers_diff_k_sorted(nums, 2)}")
    y = numbers_diff_k_sorted(nums, 2)
    (
      Stats(profile)
      .strip_dirs()
      .sort_stats(SortKey.CALLS)
      .print_stats()
    )

# with Profile() as profile:
#     # print(f"{numbers_diff_k_brute_force(nums, 2)}")
#     z = numbers_diff_k_brute_force(nums, 2)
#     (
#       Stats(profile)
#       .strip_dirs()
#       .sort_stats(SortKey.CALLS)
#       .print_stats()
#     )

# 
# print  ( nums )
# print ( x )
# print ( y )
assert( sorted(x) == sorted(y) )
# print ( sorted(z) )


# def max_three (a, b, c):
#     if a > b and a > c:
#         return a
#     if b > c:
#         return b 
#     return c
# a, b, c = 5, 1, 2
# print (max_three(a,b,c))
# a, b, c = 2, 2, 2
# print (max_three(a,b,c))
# a, b, c = 3, 2, 4
# print (max_three(a,b,c))
# a, b, c = 3, 9, 4
# print (max_three(a,b,c))