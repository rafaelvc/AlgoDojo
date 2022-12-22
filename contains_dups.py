# https://leetcode.com/problems/contains-duplicate-ii/


def contains_dups1(arr, k):
    for i in range(0, len(arr)):
        if len(arr) - i <= k:
            end = len(arr) 
        else:
            end = i+1+k
        for j in range(i+1, end):
            if arr[i] == arr[j]:
                return True
    return False

def contains_dups0(arr, k):
    positions = {}
    for i in range(0, len(arr)):
        if arr[i] not in positions:
            positions[arr[i]] = [i+1]
        else:
            (positions[arr[i]]).append(i+1)
    print (positions)
    for indexes in positions.values():
        if len(indexes) < 2:
            continue
        for i in range(0,len(indexes)):
            for j in range(i+1, len(indexes)):
                if abs(indexes[i]-indexes[j]) <= k:
                    return True
    return False
        
def contains_dups3(arr, k):
    positions = {}
    for i in range(0, len(arr)):
        if arr[i] not in positions:
            positions[arr[i]] = [i+1]
        else:
            for j in positions[arr[i]]:
                if abs((i+1)-j) <= k:
                    return True
            (positions[arr[i]]).append(i+1)
    return False


def contains_dups4(arr, k):
    positions = {}
    for i in range(0, len(arr)):
        if arr[i] not in positions:
            positions[arr[i]] = i+1
        else:
            j = positions[arr[i]]
            if abs((i+1)-j) <= k:
                return True
            positions[arr[i]] = i+1
    return False


def contains_dups2(arr, k):
    positions = {}
    for i, v in enumerate(arr):
        if v in positions and abs((i+1)-positions[v]) <= k:
            return True
        positions[v] = i+1
    return False


arr = [1,2,3,1]
print(contains_dups2(arr, k=3))

arr = [1,0,1,1]
print(contains_dups2(arr, k=1))

arr = [1,2,3,1,2,3]
print(contains_dups2(arr, k=2))
        
