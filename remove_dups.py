
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/

def remove_dups_set(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    set_result = set()
    for a in arr:
       set_result.add(a)
    return list(set_result)

def remove_dups(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    arr_result = []
    vl = arr[0]
    ix = 1
    while ix < len(arr):
        if vl != arr[ix]:
            arr_result.append(vl)
            vl = arr[ix]
        ix += 1
    arr_result.append(vl)
    return arr_result

# shrinks
def remove_dups_noextra_mem(arr):
    cur, next = 0, 0
    while next < len(arr):
        if arr[next] > arr[cur]:
            cur += 1
            arr[cur] = arr[next]
        next += 1
    return cur + 1

# removes dups at most
def remove_dups_at_most1(arr):
    cur, at_most, next, k = 0, 0, 0, 0
    while next < len(arr):
        if arr[cur] == arr[next]:
            if at_most < 2:
                at_most += 1
                k += 1
                cur += 1
            elif cur != next:
                cur = next
        else:
            arr[cur] = arr[next]
            at_most = 1
            cur += 1
            k += 1
        next += 1
    return k

def remove_dups_at_most(arr):

    prev = 0
    next = 1
    counter = 0
    k = 0
    while next < len(arr):
        if arr[prev] == arr[next]:
            counter += 1
            if counter == 2:
                prev = next
                next += 1
                while next < len(arr) and arr[prev] != arr[next]:
                    arr[prev] = arr[next]
                    prev += 1
                    next += 1
                continue 
        prev += 1
        next += 1
        

arr = [1,1,1,2,3,3,6]
print (remove_dups_at_most(arr), arr)

# arr = [0,0,1,1,1,1,2,3,3]
# print (remove_dups_at_most(arr), arr)
# arr = [1,1,2,2,3,4,4,4,5]
# print (remove_dups_at_most(arr), arr)


# arr = [1,1]
# print (remove_dups(arr))
# 
# arr = [1,1,1]
# print (remove_dups(arr))
# 
# arr = [1,2,2,2,3]
# print (remove_dups(arr))
# 
# arr = [1,1,1,2,2,2,3,3,4,4,4,4]
# print (remove_dups(arr))
# 
# arr = [1,1,1,2,2,2,3,3,4,4,4,4]
# print (remove_dups_set(arr))
# 
# 
# arr = [1,1]
# print (remove_dups_noextra_mem(arr), arr)
# 
# arr = [1,1,1]
# print (remove_dups_noextra_mem(arr), arr)
# 
# arr = [1,2,2,2,3]
# print (remove_dups_noextra_mem(arr), arr)
# 
# arr = [1,1,1,2,2,2,3,3,4,4,4,4]
# print (remove_dups_noextra_mem(arr), arr)
# 
# arr = [1,1,1,2,2,2,3,3,4,4,4,4]
# nrs = remove_dups_noextra_mem(arr)
# print (nrs, arr[:nrs])
# 
# arr = [-2,-2,-2,-1,-1,-1,4,4,4,4]
# nrs = remove_dups_noextra_mem(arr)
# print (nrs, arr[:nrs])


