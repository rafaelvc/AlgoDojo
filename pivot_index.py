# https://leetcode.com/problems/find-pivot-index/
# Solução errada... ja comecei pela ideia de slices/dois ponteiros sem verificar o brute force.
# def find_pivot(arr):
#     l, r = 0, len(arr)-1
#     sum_l, sum_r = arr[l], arr[r]
#     last_left = False
#     while l < r:
#         if sum_l > sum_r and last:
#             r -= 1
#             if r < 0:
#                 break
#             sum_r += arr[r]
#         else:
#             l += 1
#             if l == len(arr):
#                 break
#             sum_l += arr[l]
#     if sum_r == sum_l:
#         return l
#     return -1
# Aqui tem um possivel backtrack... quando se ve um possivel backtrack botar
# de lado e tentar uma solução alternativa

# Implementei Solução dada pelo Neetcode... começou com a ideia do Brute force (testar todos os 
# indices como pivot e então adaptou).
# https://www.youtube.com/watch?v=u89i60lYx8U
def find_pivot(arr):
    total = sum(arr)
    left_sum, right_sum = 0, 1
    pivotix = 0
    while pivotix < len(arr) and left_sum != right_sum:
        right_sum = (total-arr[pivotix]) - (left_sum-arr[pivotix])
        left_sum += arr[pivotix]
        pivotix += 1
    if left_sum == right_sum:
        pivotix -= 1
    else:
        pivotix = -1
    return pivotix

arr = [-1,-1,-1,-1,-1,0] # 2
print (find_pivot(arr))

arr = [1,7,3,6,5,6]
print (find_pivot(arr))

nums = [1,2,3]
print (find_pivot(nums))

nums = [2,1,-1]
print (find_pivot(nums))