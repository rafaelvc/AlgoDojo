"""
Position: Senior Py dev.

Given an integer n as input get the max number of groups of three numbers between 1..n where the two smallest squared
sumed is equal to the square of the highest value in the group. Example: For N=5, 2: (3,4,5) (4,3,5)  = 3^2 + 4^2 = 5^2

N = 10, 4: (6,8,10), (8,6,10), (3,4,5), (4,3,5)

""" 

from itertools import combinations

def max_number_of_three(n):
    
    # I forgot to use set!!!
    # squares = set([a ** 2 for a in range(1,n+1)])
    # counter = 0
    # for a in range(1,n+1):
    #     for b in range(a,n+1):
    #         if (a ** 2 + b ** 2) in squares:
    #             counter += 2
    # return counter

    # I don't need to recalculate squares
    # squares = set([a ** 2 for a in range(1,n+1)])
    # squares = [a ** 2 for a in range(1,n+1)]
    # squares_set = set(squares)
    # counter = 0
    # for a in range(1,n+1):
    #     for b in range(a,n+1):
    #         if (squares[a-1] + squares[b-1]) in squares_set:
    #             counter += 2
    # return counter

    # using combinations
    squares = [a ** 2 for a in range(1,n+1)]
    squares_set = set(squares)
    counter = 0
    for a,b in combinations(squares, 2):
        if a+b in squares_set:
            counter += 2
    return counter

print (max_number_of_three(5))
print (max_number_of_three(10))

