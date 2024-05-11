import sys
def smallest_diff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print (arr1, arr2)
    min = sys.maxsize
    pair = (None,None)

    arr1, arr2 = arr1, arr2 if len(arr1) < len(arr2) else arr2, arr1
    for i in range(len(arr1)):
        if arr1[i] < arr2[0] and abs(arr2[0]-arr1[i]) < min: 
            min = abs(arr2[0]-arr1[i]) 
            pair = (arr1[i], arr2[0])
        else: # bin search in arr1 to the near ith of arr2 jth
            for j in range(len(arr1)):


print (smallest_diff([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))