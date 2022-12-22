from typing import List 
# s and t where t is shufle of s plus extra char, what is the extra char ?
# there is a better solution, was running out of time, please Review
def solution(s: str, t: str) -> str:
    # write yout solution here
    s_counter = {}
    for c in s:
        if s_counter.get(c, None) is None:
            s_counter[c] = 1
        else:
            s_counter[c] += 1
    for c in t:
        if c not in s_counter:
            return c
        else:
            s_counter[c] -= 1
            if s_counter[c] == 0:
                del s_counter[c] # ~ O(1) https://wiki.python.org/moin/TimeComplexity
    if len(s_counter) == 0:
        return ''
    return list(s_counter.keys())[0]

print ( solution("aab", "baaa") ) 
print ( solution("aab", "baa") ) 