# https://leetcode.com/problems/summary-ranges/


def smallest_ranges(arr):
    if len(arr) == 0:
        return []
    ranges = []
    next_expected = arr[0] + 1
    cur_range = arr[0]
    for i in range(1,len(arr)):
        if arr[i] != next_expected:
            if cur_range == arr[i-1]:
                ranges.append(f'{cur_range}')
            else:
                ranges.append(f'{cur_range}->{arr[i-1]}')
            cur_range = arr[i]
            next_expected = arr[i] + 1
        else:
            next_expected += 1
    if arr[len(arr)-1] == cur_range:
        ranges.append(f'{cur_range}')
    else:
        ranges.append(f'{cur_range}->{arr[len(arr)-1]}')
    return ranges
        
nums = [0,1,2,4,5,7]
print (smallest_ranges(nums))

nums = [0,2,3,4,6,8,9]
print (smallest_ranges(nums))

nums = [1]
print (smallest_ranges(nums))
