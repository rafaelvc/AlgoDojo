# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# def first_unique(str1):
#     if len(str1) == 1:
#         return 0
#     already_checked = {}
#     for i,c in enumerate(str1):
#         if already_checked.get(c) is None:
#             if c not in str1[i+1:]:
#                 return i
#             else:
#                 already_checked[c] = 1
#     return -1

def first_unique(str1):
    letters = 26 * [0]
    start = ord('a')
    for c in str1:
        if letters [ ord(c) - start ] < 3:
            letters [ ord(c) - start ] += 1
    for ix, c in enumerate(str1):
        if letters [ ord(c) - start ] == 1:
            return ix 
    return -1   

s = "zab"
print (first_unique(s))

s = "leetcode"
print (first_unique(s))

s = "loveleetcode"
print (first_unique(s))

s = "aabb"
print (first_unique(s))