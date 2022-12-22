from typing import List 

# how many secs to travel num sequence in digits
# 1 sec == | a - b | going from num[a] to num[b] ix
def solution(digits: str, num: str) -> int:
    # write yout solution here
    if len(str) == 0 or len(num) == 0:
        return 0
    pos_digits = {}
    for i, d in enumerate(digits):
        pos_digits[d] = i
    last_pos, out = 0, 0
    for n in num:
        out += abs(pos_digits[n] - last_pos)
        last_pos = pos_digits[n]
    return out

print ( solution("2304125789", "571") ) 

