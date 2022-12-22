#https://leetcode.com/problems/license-key-formatting/

from collections import deque

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        fmt_key = deque()
        ck = k
        i = len(key)-1
        while i >= 0:
            if key[i] == '-':
                i -= 1
                continue
            fmt_key.extendleft(key[i].upper())
            ck -= 1
            i -= 1
            if ck == 0:
                fmt_key.extendleft('-')
                ck = k
        if len(fmt_key) > 0 and fmt_key[0] == '-':
            fmt_key.popleft()
        return ''.join(fmt_key)


key = "---"
print (Solution().licenseKeyFormatting(key, 1))

key = "0123456789"
print (Solution().licenseKeyFormatting(key, 1))

key = "--a-a-a-a--"
print (Solution().licenseKeyFormatting(key, 2))
            
key = "5F3Z-2e-9-w"
print (Solution().licenseKeyFormatting(key, 4))

key = "2-5g-3-J"
print (Solution().licenseKeyFormatting(key, 2))