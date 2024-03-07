# https://leetcode.com/problems/find-the-difference/

def find_diff1(s, t): # O( S ^ 2 ) = S + S-1 + S-2... S * S / 2 = 1 / 2 * S^2 = S^2
    t = list(t)
    for s1 in s:
        t.remove(s1)
    return ''.join(t)

def find_diff2(s, t): # S + T => T = S+1 => S + S + 1 => 2S + 1 => 2S => S => O(S)
    h = {}
    for s1 in s:
        c = h.get(s1,0)
        h[s1] = c + 1   
    r = ''
    for t1 in t:
        c = h.get(t1, 0)
        if c == 0:
            return t1
        h[t1] -= 1
        if h[t1] == 1:
            r = t1
    return r
        
def find_diff3(s, t): # O(SLOGS + S)
    s = sorted(s)
    t = sorted(t)
    # for i in range(len(s)-1, -1, -1):
    #     if s[i] != t[i+1]:
    #         return t[i+1]
    for i in range(0, len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[len(t)-1]


    print ("--")
    return t[0]

def find_diff(s, t): # S + T + 26 => O(S)
    f = 26 * [0]
    a = ord('a')
    for t1 in t:
        f[ord(t1) - a] += 1
    for s1 in s:
        f[ord(s1) - a] -= 1
    for i in range(0, 26):
        if f[i] == 1:
            return chr(a + i)
    return ''


print (find_diff3(s = "abcd", t = "abcde"))
print (find_diff3(s = "", t = "y"))
print (find_diff3(s = "a", t = "aa"))

print (find_diff3(s = "aabb", t = "eaabb"))