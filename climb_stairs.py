# https://leetcode.com/problems/climbing-stairs/

# Cracking code interview page 342

# Inefficient way O(2 ^ N) ??
def count_ways0(n):
    if n < 4:
        return n
    return count_ways(n-1) + count_ways(n-2)

# Using dynamic programing (dict) to save results
# of subproblems so we don't need to recompute
# ~ O ( log N )???
def count_ways(n, sub_prob=None):
    if n < 3:
        return n
    if sub_prob is None:
        sub_prob = {}
    elif n in sub_prob:
        return sub_prob[n]
    sub_prob[n] = count_ways(n-1, sub_prob) + count_ways(n-2, sub_prob)
    return sub_prob[n]

print (count_ways(2))
print (count_ways(3))