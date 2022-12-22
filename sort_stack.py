import random

# Smallests in the top
class MySortStack:

    def __init__(self):        
        self.stack = []
        
    def push_sort(self, x: int) -> None:
        if self.empty():
            self.stack.append( x )
            return
        aux = []
        while self.stack:
            top = self.pop()
            if x <= top:
                self.stack.append( top )
                self.stack.append( x )
                while aux:
                    self.stack.append( aux.pop() )
                return
            else:
                aux.append(top)
        self.stack.append( x )
        while aux:
            self.stack.append( aux.pop() )

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return None

    def top(self) -> int:
        if self.empty():
            return None
        return self.stack[len(self.stack) - 1]

    def empty(self) -> bool:
        return len(self.stack) == 0

def test_sort_stack():
    obj = MySortStack()
    raninput = [random.randint(1,10) for x in range(0,1000)]
    for x in raninput:
        obj.push_sort(x)
    result = [obj.pop() for x in range(0,len(raninput))]
    assert sorted(raninput) == result
    
obj = MySortStack()
raninput = [random.randint(1,10) for x in range(0,10000)]
for x in raninput:
    obj.push_sort(x)
result = [obj.pop() for x in range(0,len(raninput))]
print (result == sorted(raninput) )


# obj = MySortStack()
# obj.push_sort(10)
# obj.push_sort(8)
# obj.push_sort(6)
# obj.push_sort(6)
# obj.push_sort(6)
# obj.push_sort(9)
# obj.push_sort(7)
# 
# print (obj.pop())
# print (obj.pop())
# print (obj.pop())
# print (obj.pop())
# print (obj.pop())