# https://leetcode.com/problems/split-a-string-in-balanced-strings/

def find_balanced_substrs_nr(str1):
    balance, substrs_balanced, look_for = -1, 0, None
    for c in str1:
        # start a new search   
        if balance == 0 or balance == -1:
            if balance == 0:
                substrs_balanced += 1
            if c == 'R':
                look_for = 'L'
            elif c == 'L': 
                look_for = 'R'
            else:
                raise Exception('Invalid letter: {}'.format(c))
            balance = 1
        elif look_for == c:
            balance -= 1
        else:
            balance += 1
    if balance == 0:
        substrs_balanced += 1
    return substrs_balanced

print (find_balanced_substrs_nr('RLRRLLRLRL'))
print (find_balanced_substrs_nr('RLRRRLLRLL'))
print (find_balanced_substrs_nr('LLLLRRRR'))

            