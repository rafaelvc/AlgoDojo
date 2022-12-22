# https://leetcode.com/problems/print-foobar-alternately/

# solution accepted but execution time is bellow avg

from threading import Event as e
#from threading import Lock as l
#from threading import Condition as c

class FooBar:
    def __init__(self, n):
        self.foo_done = e()
        self.bar_done = e()
        self.bar_done.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.bar_done.wait()
            self.bar_done.clear()
            printFoo()
            self.foo_done.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.foo_done.wait()
            self.foo_done.clear()
            printBar() 
            self.bar_done.set()


        