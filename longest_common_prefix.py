# https://leetcode.com/problems/longest-common-prefix/

words = "Rafael Cabral"

def max_common_prefix(words):

    common_prefix_size = 0 
    for i in range(0, min([len(w) for w in words])):
        prefix_char = words[0][i]
        diff = False
        for w in words[1:]:
            if w[i] != prefix_char:
                diff = True
                break
        if not diff:
            common_prefix_size += 1
        elif i == 0:
            return ''
        else:
            break
    return words[0][:common_prefix_size]


strs = ["cir", "car"]
print (max_common_prefix(strs))

strs = ["aa", "bb", "cat", "car"]
print (max_common_prefix(strs))