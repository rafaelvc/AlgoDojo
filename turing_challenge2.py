from typing import List 
from collections import deque

# a calculator... 
def solution(seq: str) -> int:
    # write yout solution here
    result = deque()
    for s in seq:
        if s == 'C': # removes last result
            if len(result) < 1:
                continue
            result.pop()
        elif s == '+': # Sum last two store result
            if len(result) < 2:
                continue
            x = result.pop()
            y = result.pop()
            result.append( y )
            result.append( x )
            result.append( x + y )
        elif s == 'D': # double result and stores
            if len(result) < 1:
                continue
            x = result.pop()
            result.append ( x )
            result.append ( 2 * x )
        else: 
            result.append ( int(s) )
    if len(result) > 0:
        return result.pop()
    return 0

print ( solution("1") ) # 0
print ( solution("") ) # 0
print ( solution("42+D1+") ) # 13
print ( solution("42+D1C") ) # 12
print ( solution("DDD")) # 0
print ( solution("CCCC")) # 0