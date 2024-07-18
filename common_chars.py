# https://leetcode.com/problems/find-common-characters
from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counters = [Counter(words[i]) for i in range(1, len(words))]
        repeated = []
        for c in words[0]:
            found_every = True
            for counter in counters:
                if counter.get(c, None) is None or counter[c] == 0:
                    found_every = False
                    break
            if found_every:
                for counter in counters:
                    counter[c] -= 1
                repeated.append(c)
        return repeated

    # Wrong
    def commonChars0(self, words: List[str]) -> List[str]:
        counter = [0] * 26
        for w in words:
            for c in w:
                counter[ord(c)-97] += 1
        repeated = []
        for i in range(0, 26):
            if counter[i] > 0:
                nr_repeated_c = counter[i] // len(words)
                if nr_repeated_c > 0:
                    c = chr(97+i)
                    for j in range(1, nr_repeated_c+1):
                        repeated.append(c)
        return repeated

print (Solution().commonChars(["bella","label","roller"]))
print (Solution().commonChars(["cool","lock","cook"]))