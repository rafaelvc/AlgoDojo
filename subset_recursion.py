# Pag 348 Cracking code interview

def power_subset(arr, subsets, n = 0, subsize = 0):
    if len(arr) == (subsize + n):
        return
    subsets.append([])
    for i in range(n, n+subsize+1):
        subsets[len(subsets)-1].append(arr[i])
    power_subset(arr, subsets, n, subsize + 1)

def power_set(arr, allsets, n = 0):
    if n == len(arr):
        return
    power_subset(arr, allsets, n)
    power_set(arr, allsets, n+1)

arr = [1,2,3,4]
allsets = []
power_set(arr, allsets)
print (allsets)


# for i in range(0,10):
#     while (i) != 0:
#         print ('{0:b}'.format(i), i)
#         i >>= 1
# 
# [1]
# 7 (111) [2, 3, 4]

k = 7
i = 0
while k > 0:
    if (k & 1) == 1:
        print(i)
    i += 1
    k >>= 1