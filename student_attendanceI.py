# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord1(self, s: str) -> bool:
        count_l = 0
        count_a = 0
        last = ''
        for c in s:
            if c == 'A':
                count_a += 1
                if count_a >= 2:
                    return False
            if c == 'L':
                if last != 'L':
                    count_l = 1
                else:
                    count_l += 1
                    if count_l > 2:
                        return False
            last = c
        return True

    def checkRecord(self, s: str) -> bool:
        count_l, count_a, last = 0, 0, ''
        for c in s:
            if c == 'A':
                count_a += 1
            elif c == 'L' and last != 'L':
                count_l = 1
            elif c == 'L':
                count_l += 1
            if count_a >= 2 or count_l > 2:
                return False
            last = c
        return True
