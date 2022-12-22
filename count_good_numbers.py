# https://leetcode.com/problems/count-good-numbers

from math import pow
import cProfile, pstats

def powerNaive(a,n):
    i = n-1;
    r = a
    while i > 0:
        r *= a
        i -= 1
    return r

# Function to return a^n
def powerOptimised(a, n):
    # Stores final answer
    ans = 1
    while (n > 0):
        last_bit = (n & 1)
        # Check if current LSB
        # is set
        if (last_bit):
            ans = ans * a
        a = a * a
        # Right shift
        n = n >> 1
    return ans

# 
def count_good_nums(n):
    if n == 1:
        return 5
    elif n % 2 == 0:
        # return int((powerOptimised(20, n//2) % (powerOptimised(10, 9) + 7)))
        return int((powerOptimised(20, n//2) % (int(1e9) + 7)))
    else:
        # return int((powerOptimised(4, (n//2)) * powerOptimised(5, (n//2)+1)) % (powerOptimised(10, 9) + 7)) 
        # return int((powerOptimised(4, (n//2)) * powerOptimised(5, (n//2)+1)) % (int(1e9) + 7)) 
        return (powerOptimised(20, (n//2)) * 5) % (int(1e9) + 7)


# print (count_good_nums(1))
# print (count_good_nums(4))
# print (count_good_nums(50))
# print (count_good_nums(806166225460393))
a = powerOptimised(20, 403083112730196)



# profiler = cProfile.Profile()
# profiler.enable()
# #powerOptimised(10,10000)
# count_good_nums(806166225460393)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
 
# profiler = cProfile.Profile()
# profiler.enable()
# powerNaive(10,10000)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# 
# profiler = cProfile.Profile()
# profiler.enable()
# pow(10,10000)
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
