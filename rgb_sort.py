import random

def check_grouping(rgbs):
    if len(rgbs) == 0:
        return True
    cur_state = ''
    cur_state = rgbs[0]
    for c in rgbs[1:]:
        if cur_state == c:
            continue
        if cur_state == 'R' and (c == 'G' or c == 'B'):
            cur_state = c
        elif cur_state == 'G' and c == 'B':
            cur_state = c
        else:
            return False
    return True
        

def fill_letter(l, rgbs, counter, ix = 0):
    nr_l = counter.get (l, 0)
    while nr_l > 0:
        rgbs[ix] = l
        nr_l -= 1
        ix += 1
    return ix 


def group_rgb_by_counting(rgbs):
    counter = {}
    for l in rgbs:
        if counter.get(l, 0) == 0:
            counter[l] = 1
        else:
            counter[l] += 1
    ix = fill_letter('R', rgbs, counter )       
    ix = fill_letter('G', rgbs, counter, ix)       
    ix = fill_letter('B', rgbs, counter, ix)       
    

def group_rgb(rgbs):

    j = len(rgbs)-1
    i = 0 
    while i < j:
#        print (i, j)
        if rgbs[i] == 'R':
            i += 1
        elif rgbs[j] == 'R':
            rgbs[j], rgbs[i] = rgbs[i], rgbs[j]
            i += 1
            j -= 1
        else:
            j -= 1
#    print (i, j)
    j = len(rgbs)-1
    while (i < j) and rgbs[i] == 'R':
        i += 1

    while i < j:
        if rgbs[i] == 'G':
            i += 1
        elif rgbs[j] == 'G':
            rgbs[j], rgbs[i] = rgbs[i], rgbs[j]
            i += 1
            j -= 1
        else:
            j -= 1

letters  = ['R', 'G', 'B']
for i in range ( 0, 1000):
    rand_letter_list = []
    for j in range( 0, random.randrange(0, 1000) ):
        rand_letter_list.append(  letters [ random.randrange(0,len(letters)) ]  )
    print (rand_letter_list)
    # group_rgb(rand_letter_list)
    group_rgb_by_counting(rand_letter_list)
    if not check_grouping(rand_letter_list):
        print ('Wrong output:', rand_letter_list )
        break
    print (rand_letter_list)