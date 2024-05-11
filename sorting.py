import random
import cProfile, pstats
import time
# bubles max element to last position
# bubles second max element to penultimate postiion and so on.
def buble_sort(arr):
    i, n = 0, len(arr)
    while i < n-1:
        j = 0
        swap = False
        while j < (n-i-1):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        if not swap:
            return
        i += 1


def buble_sort2(nums):
    borbulha = True
    n = 0
    while borbulha: 
        borbulha = False
        n += 1
        for i in range(0,len(nums)-n):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1] 
                borbulha = True

# select the first min and place at 1st
# selects the second min from remaining and place at 2st and so on..
def select_sort(arr):
    for i in range(len(arr)):
        ix_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[ix_min]:
                ix_min = j
        arr[i], arr[ix_min] = arr[ix_min], arr[i]

# marks a sub-sorted array on the begining 
# every new element is lesser than last sub-sorted element 
# is sub-sorted in its correct position
# the sub-sorted array increases up to the entire sorted array
# Ps: If the data structure is a linked list 
#     each element from the unsorted linked list is sort inserted in 
#     a new sorted linked list (The algorithms is simpler than using Array)
def insert_sort(arr):
    ix_end = 0
    while ix_end < len(arr)-1:
        if arr[ix_end+1] < arr[ix_end]:
            ix_sub = ix_end + 1
            while arr[ix_sub] < arr[ix_sub-1] and ix_sub > 0: # Insert sub_sorted_array
                arr[ix_sub-1], arr[ix_sub]  = arr[ix_sub], arr[ix_sub-1]
                ix_sub -= 1
        ix_end += 1

def merge1(arr1, arr2):
    sorted_arr = (len(arr1) + len(arr2)) * [0]
    ix1, ix2, i = 0, 0, 0
    for i in range(len(sorted_arr)):
        if ix1 < len(arr1) and ix2 == len(arr2):
            sorted_arr[i] = arr1[ix1]
            ix1 += 1
        elif ix2 < len(arr2) and ix1 == len(arr1):
            sorted_arr[i] = arr2[ix2]
            ix2 += 1
        elif arr1[ix1] <= arr2[ix2]:
            sorted_arr[i] = arr1[ix1]
            ix1 += 1
        else:
            sorted_arr[i] = arr2[ix2]
            ix2 += 1
    return sorted_arr

def merge_sort1(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:len(arr)]
    return merge1(merge_sort1(arr1), merge_sort1(arr2))


def merge(arr1, arr2, arr, mid):

    if len(arr1) == 1 and len(arr2) == 1:
        return

    if len(arr1) >= len(arr2):
        start = mid - len(arr2)
        end = mid + len(arr1)
    else:
        start = mid - len(arr1)
        end = mid + len(arr2)
    
    ix1, ix2 = 0, 0 
    for i in range(start, end):
        if ix1 < len(arr1) and ix2 == len(arr2):
            arr[i] = arr1[ix1]
            ix1 += 1
        elif ix2 < len(arr2) and ix1 == len(arr1):
            arr[i] = arr2[ix2]
            ix2 += 1
        elif arr1[ix1] <= arr2[ix2]:
            arr[i] = arr1[ix1]
            ix1 += 1
        else:
            arr[i] = arr2[ix2]
            ix2 += 1
    
def merge_sort(arr, orig_arr=None, mid=-1):

    if len(arr) < 2:
        return

    div_ = len(arr) // 2
    arr1 = arr[:div_]
    arr2 = arr[div_:]

    if mid==-1:
        mid = div_
    
    if orig_arr is None:
        orig_arr = arr

    merge_sort( arr1, orig_arr, div_ // 2)
    merge_sort( arr2, orig_arr, div_ + (div_ // 2) )

    print (arr1, arr2, mid)
    merge (arr1, arr2, orig_arr, mid)



def mergeSortGeeksForGeeks(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSortGeeksForGeeks(L)
 
        # Sorting the second half
        mergeSortGeeksForGeeks(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# def partition(arr):
#     pivot = len(arr)-1
#     x, ix_part = 0, -1
#     while x <= pivot:
#         if arr[x] <= arr[pivot]:
#             ix_part += 1
#             arr[x], arr[ix_part] = arr[ix_part], arr[x]
#         print (arr, x, ix_part)
#         x += 1
#     return ix_part

# partition( [9,4,8,3,7,1,6,2,5] )



# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with 
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1
  
# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


# def quick_sort(arr, left_side=None, right_side=None):
#     
#     if left_side is None and right_side is None: # First cal
#         pivot = len(arr)-1
#         x = 0
#     elif left_side == -1 or right_side == len(arr): # Base case last recursion
#         return 
#     elif right_side is None: # left side
#         pivot = left_side
#         x = 0 
#     else:
#         pivot = len(arr)-1
#         x = right_side
# 
#     ix_part = x - 1
# 
#     while x < pivot:
#         if arr[x] < arr[pivot]:
#             ix_part += 1
#             arr[x], arr[ix_part] = arr[ix_part], arr[x]
#         x += 1
#     arr[pivot], arr[ix_part+1] = arr[ix_part+1], arr[x]
#     print(arr)
# 
#     quick_sort(arr, left_side=ix_part)
#     quick_sort(arr, right_side=ix_part+1)
#     
# 
# arr = [9,4,8,3,7,1,6,2,5]
# print (quick_sort(arr))

# raninput = [ random.randint(0,10) for r in 10000 * [0]  ]
# raninput = [5, 9, 1, 3, 6, 8, 10, 4]
# # raninput_sorted = merge_sort(raninput)
# 
# 
# profiler = cProfile.Profile()
# 
# profiler.enable()
# mergeSortGeeksForGeeks(raninput)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# 
# profiler.enable()
# sorted(raninput)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# 
# profiler.enable()
# merge_sort(raninput)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# print (raninput)
# 
# # arr = [2,1]
# profiler.enable()
# select_sort(raninput)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# #print (raninput)
# # # select_sort(arr)
# # print (arr)
# # 
# # arr = [1,2,3,6,7,8,9,10]
# # insert_sort(arr)
# # # select_sort(arr)
# # print (arr)
# #     
# # arr = [2,3,1,5]
# # insert_sort(arr)
# # # select_sort(arr)
# # print (arr)
# # 
# # arr = [2,3,1,2,2,2,2]
# # insert_sort(arr)
# # # select_sort(arr)
# # print (arr)
# 
# # arr = [12, 11, 13, 5, 6]
# # insert_sort(arr)
# # select_sort(arr)
# #print (arr)

# buble sorts check for 10000
raninput = [ x for x in range(0,10000) ]
random.shuffle(raninput)
raninput1 = raninput.copy()
print(id(raninput), id(raninput1))



raninput = [ x for x in range(0,10000000) ]
random.shuffle(raninput)

start = time.time()
# buble_sort(raninput)
n = 0
while n < 10000000:
    raninput[n] = n
    n += 1
end = time.time()
print (end-start)
start = time.time()
# buble_sort2(raninput1)
for n in range (0, 10000000):
    raninput[n] = n
end = time.time()
print (end-start)
# print (raninput)
# print (raninput1)
print (raninput == raninput1)



# profiler = cProfile.Profile()
# profiler.enable()
# buble_sort2(raninput)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# profiler.enable()
# buble_sort(raninput1)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# 
