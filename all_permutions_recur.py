

def all_permutations(st, ix=None):
    if ix > len(st):
        return []
    perms = all_sub_perms(st, ix)
    return perms + all_permutations(st, ix-1)
    
def all_sub_perms(st, ix=0):
    c = st[ix]
    st = st[:ix] + st[ix+1:]
    comb = [ c + st ]
    for i in range(len(st)):
        comb.append( st[:i+1] + c + st[i+1:] ) 
    return comb

print (all_sub_perms('abc'))
print (all_sub_perms('abc',1))
print (all_sub_perms('abc',2))
#print (all_permutations('abc'))



def getPerms(st):
    permutations = []
    if len(st) == 0:
        permutations.append([])
        return permutations
    first = st[0]
    remainder = st[1:]
    words = getPerms(remainder)
    for word in words:
        word = list(word)
        for j in range(0, len(word)):
            permutations.append(word.copy().insert(j, first))
    return permutations


