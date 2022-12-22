# https://leetcode.com/problems/word-pattern/
# It seems to be another one-to-one relationship (bijection)
def check_pattern( pattern, s ):
    sl = s.split()
    if len(pattern) != len(sl):
        return False
    patt_dict = {}
    s_dict = {}
    for p, w in zip(pattern, sl):
        if patt_dict.get(p) is None and s_dict.get(w) is None: 
            patt_dict[p] = w
            s_dict[w] = p
        elif not( (patt_dict.get(p) and s_dict.get(w)) and\
                  (patt_dict[p] == w and s_dict[w] == p) ):
           return False
    return True


print (check_pattern( pattern = "abba", s = "dog cat cat dog"))
print (check_pattern(pattern = "abba", s = "dog cat cat fish"))
print (check_pattern(pattern = "aaaa", s = "dog cat cat dog"))
print (check_pattern(pattern = "abba", s = "dog dog dog dog"))