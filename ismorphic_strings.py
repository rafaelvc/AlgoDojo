# https://leetcode.com/problems/isomorphic-strings/

# def build_string_count_dict(s):
#     s_dict = {}
#     for c in s:
#         count = s_dict.get(c,0)
#         if count == 0:
#             s_dict[c] = 1
#         else:
#             s_dict[c] += 1
#     return s_dict


# Copied solution
# def isIsomorphic(s, t):
#        s2t, t2s = {}, {}
#        for i in range(len(s)):
#            if s[i] in s2t and s2t[s[i]] != t[i]:
#                return False
#            if t[i] in t2s and t2s[t[i]] != s[i]:
#                return False
#            s2t[s[i]] = t[i]
#            t2s[t[i]] = s[i]
#        return True


def isIsomorphic(s: str, t: str) -> bool:
    mapping_s_t = {}
    mapping_t_s = {}
    for c1, c2 in zip(s, t):
        # Case 1: No mapping exists in either of the dictionaries
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
        # it doesn't match in either of the dictionaries or both            
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
    return True

# Wrong
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    t_dict, s_dict = {}, {}
    for ix, c in enumerate(s):
        if t_dict.get(c, 0) == 0:
            t_dict[c] = t[ix]
        elif t_dict[c] != t[ix]: 
            return False
    return True


# def is_isomorphic(s, t):
#     if len(s) != len(t):
#         return False
#     t_dict, s_dict = {}, {}
#     for ix, c in enumerate(s):
#         if c not in s_dict and t[ix] not in t_dict: 
#             s_dict[c] = t[ix]
#             t_dict[ t[ix] ] = c
#         elif not (s_dict[c] == t[ix] and t_dict [ t[ix] ] == c):
#             return False
#     return True




    # s_dict = build_string_count_dict(s)
    # t_dict = build_string_count_dict(t)
    # return sorted( list(s_dict.values()) ) == sorted ( list(t_dict.values()) )

def myIsomorphic(s, t):
    s_dict, t_dict = {}, {}
    for ix, sc in enumerate(s):
        tc = t[ix]
        if sc not in s_dict and tc not in t_dict:
            s_dict[sc] = tc
            t_dict[tc] = sc
            continue
        if s_dict.get(sc) != tc or t_dict.get(tc) != sc:
          return False
    return True


s, t = "egg", "add"
print (isIsomorphic(s, t))

s, t = "foo", "bar"
print (isIsomorphic(s, t))

s, t = "paper", "title"
print (isIsomorphic(s, t))

# s, t = "ac", "b"
# print (isIsomorphic(s, t))

s, t = 'aba','ggd'
print (isIsomorphic(s, t))

s, t = 'badc','baba'
print (isIsomorphic(s, t))

s, t = 'aaab','cddd'
print (isIsomorphic(s, t))

s, t = 'ad','da'
print (isIsomorphic(s, t))


print ('.....................')

s, t = "egg", "add"
print (myIsomorphic(s, t))

s, t = "foo", "bar"
print (myIsomorphic(s, t))

s, t = "paper", "title"
print (myIsomorphic(s, t))

# s, t = "ac", "b"
# print (myIsomorphic(s, t))

s, t = 'aba','ggd'
print (myIsomorphic(s, t))

s, t = 'badc','baba'
print (myIsomorphic(s, t))

s, t = 'aaab','cddd'
print (myIsomorphic(s, t))

s, t = 'ad','da'
print (myIsomorphic(s, t))

