#https://leetcode.com/problems/length-of-last-word/

def last_word_len(sentence):

    lw_counter = 0
    i = len(sentence) - 1
    while sentence[i] == ' ' and i >= 0:
        i -= 1
    while i >= 0:
        if sentence[i] == ' ':
            break
        lw_counter += 1
        i -= 1
    return lw_counter


s = "Hello World            "
print(last_word_len(s))

s = "   fly me   to   the moon  "
print(last_word_len(s))