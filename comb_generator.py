# Hacker Rank easy problem ( given a string remove all two letters and
# return max string after removing the two with only alternating letters)

# str_ = "Rafael"
# letters_dict = {}
# for g in str_: 
    # count = letters_dict.get(g, 0)
    # if count > 0:
       # letters_dict[g] += 1 
    # else:
        # letters_dict[g] = 1

# keys = [ k for k in letters_dict.keys() ]
# for k in range(0, len(keys)):
    # for j in range(k+1, len(keys)):
        # print (keys[k], keys[j])

# print ('----------------------')
# letter_set = set()
# for g in str_: 
    # letter_set.add(g)

# letter_list = list(letter_set)
# for k in range(0, len(letter_list)):
    # for j in range(k+1, len(letter_list)):
        # print (letter_list[k], keys[j])


def two_letter_combination_generator(word):
    letter_set = set()
    for g in word: 
        letter_set.add(g)
    letter_list = list(letter_set)
    for k in range(0, len(letter_list)):
        for j in range(k+1, len(letter_list)):
            yield letter_list[k], letter_list[j]

# for l1, l2 in two_letter_combination_generator(word="Rafael"):
#        print (l1, l2)

# print (sorted(two_letter_combination_generator(word="Rafael")))

def check_alternates(w):
    if len(w) < 2:
        return True
    l = w[0]
    for c in w[1:]:
        if c == l:
            return False
        l = c
    return True

# word = 'abaaab'
# letter_set = set()
# for g in word: 
    # letter_set.add(g)
# for l in letter_set:
    # w1 = word
    # w1.replace(l, '')
# print (check_alternates(word))

word = 'ab'
cur_max = 0
for l1, l2 in two_letter_combination_generator(word):
    word_without_l1l2 = word.replace(l1,'').replace(l2, '')
    if check_alternates(word_without_l1l2):
        cur_max = max(len(word_without_l1l2), cur_max)

print (cur_max)


