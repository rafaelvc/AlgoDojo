# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
import cProfile, pstats, random

def longest_consecutive_ones_(arr):

    return max([len(ones) for ones in arr.split('0')]) >\
           max([len(zeros) for zeros in arr.split('1')])


def longest_consecutive_ones(arr):
    max_consec_one, max_consec_zero, ones, zeroes = 0,0,0,0
    for n in arr:
        if ones > 0 and n == '0':
            max_consec_one = max (ones, max_consec_one) # + ~0.015 s
            # if ones > max_consec_one:
            #    max_consec_one = ones
            ones, zeroes = 0, 1
        elif zeroes > 0 and n == '1':
            max_consec_zero = max (zeroes, max_consec_zero)  # + ~0.015 s
            # if zeroes > max_consec_zero:
            #    max_consec_zero = zeroes
            ones, zeroes = 1, 0
        elif n == '0':
            zeroes += 1
        # elif n == '1':
        else:
            ones += 1

    if ones and ones > max_consec_one:
        max_consec_one = ones
    elif zeroes and zeroes > max_consec_zero:
        max_consec_zero = zeroes

    return max_consec_one > max_consec_zero

# s = "1101"
# print (longest_consecutive_ones_(s))
# 
# s = "111000"
# print (longest_consecutive_ones_(s))
# 
# s = "110100010"
# print (longest_consecutive_ones_(s))

profiler = cProfile.Profile()
raninput = ''.join([str(random.randint(0,1)) for r in 100000 * [0]])
# print (raninput)

profiler.enable()
print (longest_consecutive_ones(raninput))
profiler.disable()
# stats = pstats.Stats(profiler).sort_stats('ncalls')
# stats.print_stats()
stats = pstats.Stats(profiler).get_stats_profile()
print (stats.total_tt)

profiler.enable()
print (longest_consecutive_ones_(raninput))
profiler.disable()
# stats = pstats.Stats(profiler).sort_stats('ncalls')
# stats.print_stats()
stats = pstats.Stats(profiler).get_stats_profile()
print (stats.total_tt)



