# https://leetcode.com/problems/isomorphic-strings/

class Solution:

    def isIsomorphic0(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        for cs, ct in zip(s, t):
            if s_to_t.get(cs, None) is None:
                if ct in s_to_t.values():
                    return False
                s_to_t[cs] = ct
            elif s_to_t[cs] != ct:
                return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = [None]*95
        t_to_s = [None]*95
        for cs, ct in zip(s, t):
            if s_to_t[ord(cs)-48] is None:
                if t_to_s[ord(ct)-48] != None and t_to_s[ord(ct)-48] != cs:
                    return False
                s_to_t[ord(cs)-48] = ct
                t_to_s[ord(ct)-48] = cs
            elif s_to_t[ord(cs)-48] != ct:
                return False
        return True


print (Solution().isIsomorphic("egg", "add"))
print (Solution().isIsomorphic("foo", "bar"))
print (Solution().isIsomorphic("paper", "title"))
print (Solution().isIsomorphic("badc", "baba"))