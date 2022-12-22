# https://leetcode.com/problems/repeated-substring-pattern


def repeated_substr(astr):
    if len(astr) == 1:
        return False
    for i in range(1, (len(astr) // 2) + 1):
        if len(astr) % i == 0:
            # nrsubs = len(astr) // i
            # if astr[:i] * nrsubs == astr:
            #    return True
            found = True
            for j in range(i,len(astr), i):
                # print (astr[j:j+i], astr[:i])
                if astr[j:j+i] != astr[:i]:
                    found = False
                    break 
            if found:
                return True
    return False

s = "a"
print (repeated_substr(s))

s = "aaaaaaaaaaaaa"
print (repeated_substr(s))

s = "abab"
print (repeated_substr(s))

s = "abaaba"
print (repeated_substr(s))

s = "abcdabcd"
print (repeated_substr(s))

s = "aba"
print (repeated_substr(s))
