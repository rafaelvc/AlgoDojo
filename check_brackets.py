# https://leetcode.com/problems/valid-parentheses/
from collections import deque


def is_valid(s):
    brack_stack = deque()
    for c in s:
        if c == '{' or c == '[' or c == '(':
            brack_stack.appendleft(c)
        elif len(brack_stack) == 0:
            return False 
        else:
            c1 = brack_stack.popleft()
            if (c == '}' and c1 != '{') or\
               (c == ')' and c1 != '(') or\
               (c == ']' and c1 != '['):
                return False
    if len(brack_stack) == 0:
        return True
    return False
            
        
s = "({{{}{}}})"
print (is_valid(s))

s = "()[]{}"
print (is_valid(s))
