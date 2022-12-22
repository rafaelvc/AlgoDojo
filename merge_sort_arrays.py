
def merge_sort_arrays(arr1, arr2, m, n):

    ix = (n + m) - 1
    n -= 1
    m -= 1
    while ix >= 0:
        if n >= 0 and m >= 0:
            if arr2[n] >= arr1[m]:
                arr1[ix] = arr2[n]
                n -= 1
            else:
                arr1[ix] = arr1[m]
                m -= 1
        elif n == -1:
            arr1[ix] = arr1[m]
            m -= 1
        else:
           arr1[ix] = arr2[n]
           n -= 1
        ix -= 1


nums1 = [2,2,3,0,0] 
m = 3 
nums2 = [5,6] 
n = 2
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [1,2,0,0,0]
m = 2
nums2 = [4,5,6]
n = 3
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [1,0]
m = 1
nums2 = [2]
n = 1
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [2,4,6,0,0,0]
m = 3
nums2 = [1,3,5]
n = 3
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [1,3,5,0,0,0]
m = 3
nums2 = [2,4,6]
n = 3
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [2,4,6,0,0,0,0]
m = 3
nums2 = [1,3,5,7]
n = 4
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)

nums1 = [2,4,6,7,0,0,0]
m = 4
nums2 = [1,3,5]
n = 3
merge_sort_arrays(nums1, nums2, m, n)
print (nums1)








