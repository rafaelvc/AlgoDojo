# https://leetcode.com/problems/assign-cookies/

def assign_cookies(g, s):
    g.sort()
    s.sort()
    out, j = 0, 0
    for i in g:
        while j < len(s) and s[j] < i:
            j += 1
        if j == len(s):
            return out
        elif s[j] >= i:
            out += 1
            j += 1
    return out

print (assign_cookies(g = [1,2,3], s = [1,1]))
print (assign_cookies(g = [1,2], s = [1,2,3]))
print (assign_cookies(g = [10,9,8,7], s = [5,6,7,8]))