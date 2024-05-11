# Page 71 - given a string of unique chars generate all permutations

# abc, bac, cab 

# def all_perms(astr):
#     words = [astr]
#     for i in range(0, len(astr)):
#         for j in range(0, len(astr)):
#             if i == j:
#                 continue
#             words.append( astr[0:j-1] + astr[j] + astr[i] + astr[j+1:])
#     return words
            
        
# print (all_perms("abcdefg"))

# def func1(astr):
#     perms = set()
#     astr1 = list(astr)
#     for j in range(len(astr1)):
#         astr = list(astr1)
#         if j > 0:
#             astr[0], astr[j] = astr[j], astr[0]
#         st = ''.join(astr)  
#         print(st)
#         if st not in perms:
#             perms.add(st)
# 
#         for i in range(len(astr)-1):
#             astr[i], astr[i+1] = astr[i+1], astr[i]
#             st = ''.join(astr)  
#             print (st)
#             if st not in perms:
#                 perms.add(st)

#    print (perms)
# func1("abcd")


# https://leetcode.com/problems/permutations

import random as rd

# def generate_a_perm(alist):
#         if alist == []:
#              return
#         for ix, a in enumerate(alist): 
#             print(a)    
#             if ix + 1 < len(alist):
#                 generate_a_perm( alist[ix+1:] )
# generate_a_perm([1,2,3])


def generate_a_perm(alist, sublist=None):
    if len(alist) == 0:
         return sublist
    n = rd.sample(alist, 1)[0]
    del alist[alist.index(n)]
    if sublist is None:
         sublist = [n]
    else:
         sublist.append(n)
    return generate_a_perm(alist, sublist)

def perm(alist):
    result = []
    while len(alist) > 0:
        n = rd.sample(alist, 1)[0]
        del alist[alist.index(n)]
        subperm = generate_a_perm(list(alist))
        if subperm is not None:
            subperm.append(n)
            result.append(subperm)
    return result

def aperm(parcialperm, remaining):
    if len(remaining) == 0:
        return parcialperm
    parcialperm.append(remaining.pop())
    return aperm( parcialperm, remaining )


def bperm(nlist, result, a=0, b=None, p=None):
    if b is None:
        b = len(nlist)
    if a >= b:
        return p
    for ix in range(a, b):
        nlist[a], nlist[ix] = nlist[ix], nlist[a]
        # print (nlist[a])
        if p is None:
            p = [nlist[a]]
            prefix = list(p)
        else:
            prefix = list(p)
            p.append(nlist[a])
        # parcialperm = []
        # result.append ( aperm( parcialperm, list(nlist) ) )
        perm = bperm(nlist, result, a+1, b, p)
        if perm is not None:
            result.append(perm)
        p = prefix
        nlist[a], nlist[ix] = nlist[ix], nlist[a] # undo swap

# result = []
# bperm([1,2,3,4], result)
# print (result, len(result))
# 
# 
# result = []
# bperm([1,2,3], result)
# print (result, len(result))


# check for repetitive permissions
# while len(result) > 0:
#     p = result.pop() 
#     if p in result:
#         print ('Repetitive:', p)
#         break
# else:
#     print ('No repetitions')


def newperm(nlist, result, prefix=None, a=0):
    if a == len(nlist):
        return True
    if prefix is None:
        prefix = [0] * len(nlist)
    for i in range(a, len(nlist)):
        nlist[a], nlist[i] = nlist[i], nlist[a]
        prefix[a] = nlist[a]
        ret = newperm(nlist, result, prefix, a+1)
        if ret:
            result.append(list(prefix))
        nlist[a], nlist[i] = nlist[i], nlist[a]
    return False

result = []
newperm([1,2,3,], result)
print (result, len(result))

result = []
newperm([1,2,3,4], result)
print (result, len(result))


def generate_permutations(nlist, perms, prefix=None, ss=0):
    if ss == len(nlist): # ss (sufix start)
        return True
    if prefix is None:
        prefix = [0] * len(nlist)
    for i in range(ss, len(nlist)):
        nlist[ss], nlist[i] = nlist[i], nlist[ss] # brings next new root
        prefix[ss] = nlist[ss]
        if generate_permutations(nlist, perms, prefix, ss+1):
            perms.append(list(prefix))
        nlist[ss], nlist[i] = nlist[i], nlist[ss] # undo the root
    return False

result = []
generate_permutations([1,2,3,], result)
print (result, len(result))

result = []
generate_permutations([1,2,3,4], result)
print (result, len(result))

