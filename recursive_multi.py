

def mult0(a,b):
    if b == 0:
        return 0
    return a + mult(a, b-1)

# Recursive tail - enables recursive tail optimization for some compilers, Python requires sys.setrecursionlimit
# prevents stacks overflow
def mult(a,b, total=0):
    if b == 0 or a == 0:
       return total
    if abs(a) < abs(b): # It is better to sum 1 million two times than one millions times two
        b, a = a, b
    if b < 0:
        b = -b
        a = -a
    return mult(a, b-1, (total+a))


print (mult0(3,3))
print (mult(3,3))
print (mult(7,6))
print (mult(1,2))
print (mult(2,1))

print (mult(3,-3))
print (mult(-3,3))
print (mult(-3,-3))
print (mult(0,1))
print (mult(2, -1000000000))