import multiprocessing as mp
import time
import functools
# import sys
# sys.set_int_max_str_digits(641)
from dataclasses import dataclass, field
import os

# def timetracker(f, *args, **kwargs):
def timetracker(f):
    # @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = f(*args, **kwargs)
        end = time.time()-start
        print (f"{f.__name__} :", end)
        return r
    return wrapper

@timetracker
def f1(z):
    return sum( [x**x for x in range(0,10000)] )

def f2(r):
    r.value = sum( [x**x for x in range(0,2000)] )

def f3(r):
    r.value = sum( [x**x for x in range(2000,4000)] )

def f4(r):
    r.value = sum( [x**x for x in range(4000,6000)] )

def f5(r):
    r.value = sum( [x**x for x in range(6000,8000)] )

def f6(r):
    r.value = sum( [x**x for x in range(8000,10000)] )

def fPoolable(array):
    return sum ([x**x for x in array])

@timetracker
def fParallel():
    r1, r2, r3, r4, r5  = mp.Value('i', 0), mp.Value('i', 0), mp.Value('i', 0), mp.Value('i', 0), mp.Value('i', 0) 
    p1 = mp.Process(target=f2, args=(r1,))
    p2 = mp.Process(target=f3, args=(r2,))
    p3 = mp.Process(target=f4, args=(r3,))
    p4 = mp.Process(target=f5, args=(r4,))
    p5 = mp.Process(target=f6, args=(r5,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    return r1.value + r2.value + r3.value + r4.value + r5.value

@timetracker
def fParallelPoolable():
    workers = 4 
    size = 10000
    step = size // workers 
    with mp.Pool(processes=workers) as pool:
        # return sum ( pool.map(fPoolable, [range(2000), range(2000, 4000), range(4000, 6000), range(6000, 8000), range(8000, 10000)]) )
        return sum(pool.map(fPoolable, [range(x, x+step) for x in range(0, size, step)]))

@dataclass
class AClassThatDoesMP:
    result : int = 0
    workers: int = 4 # number of leet code cores
    size: int = 10000
    worker_name: str = 'Worker0'

    def fPoolable(self, array):
        if array[0] == 2500:
            self.worker_name = 'Worker1'
        elif array[0] == 5000:
            self.worker_name = 'Worker2'
        elif array[0] == 7500:
            self.worker_name = 'Worker3'
        print (self, id(self), os.getpid())   
        return sum([x**x for x in array])

    # There is an issue with the distribution... 2 workers will get easier tasks (it is likely that 2^2 is easier to calculate than 1000 ^ 1000) 
    # We need to find a way to better distribute the inputs among the workers
    @timetracker
    def fParallelPoolable(self):
        step = self.size // self.workers
        with mp.Pool(processes=self.workers) as pool:
            self.result = sum(pool.map(self.fPoolable, [range(x, x+step) for x in range(0, self.size, step)]))
 
    def __post_init__(self):
        # a Validation for workers
        # get number of cores and dont allow a number greater than x cores availables
        if self.size > 10000:
            raise ValueError("I can't solve problems with size greater than 10000")
        
if __name__ == '__main__':
    f1(None)
    # fParallel()
    # fParallelPoolable()
    # AClassThatDoesMP(workers=2).fParallelPoolable()
    a = AClassThatDoesMP(workers=4)
    a.fParallelPoolable()
    print (a.worker_name, id(a), os.getpid())
    # AClassThatDoesMP(workers=8).fParallelPoolable()


   






