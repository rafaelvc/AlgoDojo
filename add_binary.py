# https://leetcode.com/problems/add-binary


from collections import deque
# binary addition rules
def digit_add(a, b, carry):
    # if a == '0'and b == '0':
    #     if carry:
    #         return False, '1'
    #     return False, '0'
    # elif a == '1' and b == '1':
    #     if carry:
    #         return True, '1'
    #     return True, '0'
    # if carry:
    #     return True, '0'
    # return False, '1'
    if a == b:
        return True if a == '1' else False, '1' if carry else '0'
    if carry:
        return True, '0'
    return False, '1'

def add_bin(a, b):
    a, b = list(a), list(b)
    if len(a) > len(b):
        a, b = b, a
    carry, j = False, len(b)-1
    for i in range(len(a)-1, -1, -1):
       carry, digit = digit_add(a[i], b[j], carry)
       b[j] = digit
       j -= 1
    while j > -1 and carry:
        carry, digit = digit_add(b[j], '0', carry)
        b[j] = digit
        j -= 1
    if carry:
        return '1' + ''.join(b)
    return ''.join(b)

def add_bin1(a, b):
    # result = deque()
    if len(a) >= len(b):
        a, b = list(b), list(a)
    else:
        a, b = list(a), list(b)
    j = len(b)-1
    carry = False
    for i in range(len(a)-1, -1, -1):
       carry, digit = digit_add(a[i], b[j], carry)
       # result.appendleft(digit)
       b[j] = digit
       j -= 1
    while j > -1 and carry: # remove 'and carry' if deque
        carry, digit = digit_add(b[j], '0', carry)
        #result.appendleft(digit)
        b[j] = digit
        j -= 1
    if carry:
        return '1' + ''.join(b)
        # result.appendleft('1')
    return ''.join(b)
   # return ''.join(result)



print (add_bin(a = "11", b = "1"))
print (add_bin(a = "1010", b = "1011"))
print (add_bin(a = "1111", b = "1111"))