# https://leetcode.com/problems/happy-number/

def poweroftwo_cache(nr, cache):
    if nr in cache:
        return cache[nr]
    cache[nr] = nr ** 2
    return cache[nr]

# max recursion limit reached
def happy_nr(nr, ptwocache = None):
    if nr == 1:
        return True
    # elif len(str(nr)) == 1:
    #    return False
    if ptwocache is None:
        ptwo_cache = {}
    result = sum ([ poweroftwo_cache( int(digit), ptwo_cache ) for digit in str(nr) ])
    return happy_nr(result, ptwocache)

# Accepted 
def happy_nr(nr):
    ptwo_cache = {}
    result_set = set()
    while nr != 1:
        nr = sum ([poweroftwo_cache( int(digit), ptwo_cache ) for digit in str(nr)])
        if nr in result_set: # repeated result... got a cycle ?
            return False
        result_set.add( nr )
    return True



print (happy_nr(19))
print (happy_nr(2))
print (happy_nr(22222222222222222222222222222222222222222222222222222222222))