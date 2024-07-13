from collections import defaultdict, Counter
from collections import deque
import heapq as h
from dataclasses import dataclass

class A:
    def __init__(self):
        self.aprop = 10
        print ("A")
class B(A):
    pass
    # def __init__(self):
    #     super().__init__()
    #     print ("B")
a = B()
print (a.aprop)

x = "12345"
print (x[3::-1])
print (x[::2])

# z = Counter()
z = defaultdict(int)
str_ = "aaabbc"
for c in str_:
   z[c] += 1
print (z, z['d'])

z = dict([(1,2), (2,3)])
print (z[1])

for k,v in z.items():
    print (k,v)

del z[1]
print (3 in z.values())
print (z.get(2,0))

k = defaultdict(list)
print (k['a'])


j = Counter([1,1,1,2,3,3])
print (j.most_common())


dq = deque([1,2,3])
print ( dq.pop() )
print( dq.popleft() )
dq1 = [1,2,3]
print (dq1.pop())
dq.appendleft(4)
print (dq)

k = []
h.heappush(k, 2)
h.heappush(k, 10)
print (k)

l = [1, 1, 2, 3, 5, 9, 4, 6, 5]
for i in range(len(l)):
    print (h.heappop(l), end = " ")


@dataclass
class Employee:
    name : str
    salary : int
    role : str


print ( Employee("Rafael", 100000, "Dev") )
e = Employee("Rafael", 100000, "Dev") 



