# https://leetcode.com/problems/arranging-coins

def arraning_coins(coins):

    last_step = 0
    while  (last_step + 1) <= coins:
        last_step += 1
        coins -= last_step 
    return last_step

print (arraning_coins(8))