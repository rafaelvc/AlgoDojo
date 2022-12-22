# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue2:

    def __init__(self):        
        self.stack = []
        self.stack_aux = []
        self.size = 0
        
    def push(self, x: int) -> None:

        self.size += 1
        while self.stack_aux:
            self.stack.append( self.stack_aux.pop() )
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return 0
        if len(self.stack_aux) == 0:
            while self.stack:
                self.stack_aux.append ( self.stack.pop() )
        self.size -= 1
        return self.stack_aux.pop()
        
    def peek(self) -> int:
        if self.empty():
            return 0
        if self.stack_aux:
            return self.stack_aux[self.size - 1]
        return self.stack[0]

    def empty(self) -> bool:
        return self.size == 0


class MyQueue3:

    def __init__(self):        
        self.stack = []
        self.stack_aux = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return 0
        if len(self.stack_aux) == 0:
            while self.stack:
                self.stack_aux.append ( self.stack.pop() )
        return self.stack_aux.pop()
    
    def peek(self) -> int:
        if self.empty():
            return 0
        if self.stack_aux:
            return self.stack_aux[len(self.stack_aux) - 1]
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.stack_aux) == 0


class MyQueue4:

    def __init__(self):        
        self.stack = []
        self.stack_aux = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def __shift_stack(self):
        while self.stack:
            self.stack_aux.append(self.stack.pop())
            
    def pop(self) -> int:
        if self.empty():
            return 0
        if len(self.stack_aux) == 0:
            self.__shift_stack()
        return self.stack_aux.pop()
    
    def peek(self) -> int:
        if self.empty():
            return 0
        if len(self.stack_aux) == 0:
            self.__shift_stack()
        return self.stack_aux[len(self.stack_aux) - 1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.stack_aux) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


obj = MyQueue4()
obj.push(1)
obj.push(2)
obj.push(3)

print (obj.empty())
print (obj.peek())
print (obj.pop())
print (obj.empty())
print (obj.peek())
print (obj.pop())
print (obj.empty())
print (obj.peek())
print (obj.pop())
print (obj.empty())

obj.push(1)
obj.push(2)
obj.push(3)

print (obj.empty())
print (obj.peek())
print (obj.pop())
print (obj.empty())
print (obj.peek())
print (obj.pop())
print (obj.empty())
print (obj.peek())
print (obj.pop())
print (obj.empty())