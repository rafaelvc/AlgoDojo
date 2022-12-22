# https://leetcode.com/problems/image-smoother/
from math import floor

def image_smoother(mat):
    newmat = [row[:] for row in mat] # Create a copy of the matrix
    #from copy import deepcopy
    #newmat = deepcopy(mat)
    n = len(mat)
    m = len(mat[0])
    if n > 1 and m > 1:
        for i in range(0, n):
            for j in range(0, m):
                # corner detection
                if i == 0 and j == 0:
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j+1] + mat[i+1][j+1] + mat[i+1][j]) / 4 )
                elif i == 0 and j == m-1:
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j-1] + mat[i+1][j-1] + mat[i+1][j]) / 4 )
                elif i == n-1 and j == 0:
                    newmat[i][j] = floor( (mat[i][j] + mat[i-1][j] + mat[i-1][j+1] + mat[i][j+1]) / 4 )
                elif i == n-1 and j == m-1:
                    newmat[i][j] = floor( (mat[i][j] + mat[i-1][j] + mat[i-1][j-1] + mat[i][j-1]) / 4 )
                elif i == 0: # up 
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j-1] + mat[i][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]) / 6 )
                elif i == n-1: # dow
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j-1] + mat[i][j+1] + mat[i-1][j-1] + mat[i-1][j] + mat[i-1][j+1]) / 6 )
                elif j == 0: # left
                    newmat[i][j] = floor( (mat[i][j] + mat[i-1][j] + mat[i+1][j] + mat[i-1][j+1] + mat[i][j+1] + mat[i+1][j+1]) / 6 )
                elif j == m-1: # rigth
                    newmat[i][j] = floor( (mat[i][j] + mat[i+1][j] + mat[i-1][j] + mat[i-1][j-1] + mat[i][j-1] + mat[i+1][j-1]) / 6 )
                else: # midle
                    newmat[i][j] = floor( (mat[i][j] + mat[i-1][j-1] + mat[i-1][j] + mat[i-1][j+1] + mat[i][j-1] + mat[i][j+1] + mat[i+1][j-1] + mat[i+1][j] + mat[i+1][j+1]) / 9 )
    elif n == 1 and m == 1:
        return newmat
    elif n == 1:
        for i in range(0, n):
            for j in range(0, m):
                # corner detection
                if i == 0 and j == 0:
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j+1] ) / 2 )
                elif i == 0 and j == m-1:
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j-1] ) / 2 )
                else:
                    newmat[i][j] = floor( (mat[i][j] + mat[i][j-1] + mat[i][j+1]) / 3 )
    else:
        for i in range(0, n):
            for j in range(0, m):
                # corner detection
                if i == 0 and j == 0:
                    newmat[i][j] = floor( (mat[i][j] + mat[i+1][j] ) / 2 )
                elif i == n-1 and j == 0:
                    newmat[i][j] = floor( (mat[i][j] + mat[i-1][j] ) / 2 )
                else:
                    newmat[i][j] = floor( (mat[i][j] + mat[i+1][j] + mat[i-1][j]) / 3 )
    return newmat

img = [[1,1,1],[1,0,1],[1,1,1]]
print (image_smoother(img))

img = [[100,200,100],[200,50,200],[100,200,100]]
print (image_smoother(img))

img = [[1,2],[3,4],[5,6]]
print (image_smoother(img))

img = [[1,3,5,7,9], [2,4,6,8,10]]
print (image_smoother(img))

img = [[3],[2],[1]]
print (image_smoother(img))

img = [[3,2,1,5,4]]
print (image_smoother(img))