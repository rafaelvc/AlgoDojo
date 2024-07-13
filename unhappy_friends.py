# https://leetcode.com/problems/count-unhappy-friends/

from typing import List

class Solution:

    def unHappy(self, preferences, x, y, dicx, dicy):
        x_pref = preferences[x]
        pref_x = x_pref.index(y) 
        if pref_x > 0: # y is not a preference
            for i in range(pref_x+1):
                pref = x_pref[i]
                partner = dicx[pref] if pref in dicx.keys() else dicy[pref]
                if preferences[pref].index(x) < preferences[pref].index(partner):
                    return 1
        return 0
    
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dicx = dict( pairs )
        dicy = dict( [[y,x] for x,y in pairs] )
        unhappy = 0
        for x,y in pairs:
            unhappy += (self.unHappy(preferences, x, y, dicx, dicy) + self.unHappy(preferences, y, x, dicx, dicy))
        return unhappy

    
print (Solution().unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]))
print (Solution().unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]]))
print (Solution().unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))
            