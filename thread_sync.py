# https://leetcode.com/problems/print-in-order/
# Syncronization mechanisms locks, conditions, events, semaphores

from threading import Event as e

class Foo:

    def __init__(self):
        self.first_done = e()
        self.sec_done = e()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_done.wait()
        printSecond()
        self.sec_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.sec_done.wait()
        printThird()