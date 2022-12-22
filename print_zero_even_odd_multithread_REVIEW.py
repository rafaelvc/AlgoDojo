# https://leetcode.com/problems/print-zero-even-odd/

from threading import Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.counter = 0
        self.even_cond = Condition()
        self.odd_cond = Condition()
        self.zero_cond = Condition()
        self.restart_cond = Condition()
    # 010203
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        
        printNumber(0)
        with self.zero_cond:
            self.zero_cond.notify_all()
        with self.even_cond:
            self.even_cond.wait()
        printNumber(0)
        with self.odd_cond:
            self.odd_cond.notify_all()
        with self.restart_cond as rc:
            self.restart_cond.wait()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
        with self.zero_cond:
            self.zero_cond.wait()
        printNumber(self.counter)
        self.counter += 1
        with self.even_cond:
            self.even_cond.notify_all()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:

        with self.zero_cond:
            self.zero_cond.wait()
        with self.odd_cond:
            self.odd_cond.wait()
        printNumber(self.counter)
        self.counter += 1
        with self.restart_cond:
            self.restart_cond.notify_all()