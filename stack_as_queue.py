
#https://leetcode.com/problems/implement-stack-using-queues/

# Future version improvement: 
# Both queue and queue_aux remains in memory at its 
# max reached stack size. So we might decrease
# the queues sizes when a pop is done.

class MyStack:

    def __init__(self):        
        self.queue = []
        self.queue_aux = []
        self.is_main_queue = True
        self.size = 0
        
    def __pick_queue(self):        
        if self.is_main_queue:        
            return self.queue, self.queue_aux
        else:
            return self.queue_aux, self.queue
        
    def push(self, x: int) -> None:
        self.size += 1
        queue, qaux = self.__pick_queue()
        if self.size > len(queue):
            queue.append(x)
        else:
            queue[self.size - 1] = x

    def pop(self) -> int:
        if self.empty():
            return 0
        queue, queue_aux = self.__pick_queue()
        for ix in range(0, self.size):
            if ix + 1 == self.size:
                result = queue[ix] 
                queue[ix] = 0
                break
            elif ix + 1 > len(queue_aux):
                queue_aux.append( queue[ix] )
            else:
                queue_aux[ix] = queue[ix] 
            queue[ix] = 0
        self.size -= 1
        self.is_main_queue = not self.is_main_queue
        return result
        
    def top(self) -> int:
        if self.empty():
            return 0
        queue, qaux = self.__pick_queue()
        return queue[self.size - 1]

    def empty(self) -> bool:
        return self.size == 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)

print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())

obj.push(1)
obj.push(2)
obj.push(3)

print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())

obj.push(1)
obj.push(2)
obj.push(3)

print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())
print (obj.top())
print (obj.pop())
print (obj.empty())

