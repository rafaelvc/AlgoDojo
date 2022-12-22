# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/


def count_consecutive_ones(arr):
    max_consec = 0
    cur_counter = 0
    for n in arr:
        if n == 1:
            cur_counter += 1
        elif n == 0 and cur_counter > 0:
            if cur_counter >= max_consec:
                max_consec = cur_counter
            cur_counter = 0
    if cur_counter >= max_consec:
        max_consec = cur_counter
    return max_consec


nums = [1,1,0,1,1,1]
print (count_consecutive_ones( nums ))

nums = [1,0,1,1,0,1]
print (count_consecutive_ones( nums ))
