# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/
from collections import defaultdict
from collections import Counter

class Solution:

    def maxFreq0(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrs = defaultdict(int)
        max_str = 0
        for size in range(minSize, maxSize+1):
            for j in range(0, (len(s)-size)+1):
                substr = s[j:j+size]
                if len(set(substr)) <= maxLetters:
                    substrs[substr] += 1
                    if substrs[substr] > max_str:
                        max_str = substrs[substr]
        return max_str

    # Sim eu tinha a intuição de que só bastava iterar sobre minsize 
    # pois a tendencia é ter mais substrings menores do que maiores
    # https://algo.monster/liteproblems/1297        
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrs = Counter()
        max_str = 0
        for j in range(0, (len(s)-minSize)+1):
            substr = s[j:j+minSize]
            if len(set(substr)) <= maxLetters:
                substrs[substr] += 1
                if substrs[substr] > max_str:
                    max_str = substrs[substr]
        return max_str

print (Solution().maxFreq("aababcaab", maxLetters = 2, minSize = 3, maxSize = 4) )
print (Solution().maxFreq("aaaa", maxLetters = 1, minSize = 3, maxSize = 3) ) 