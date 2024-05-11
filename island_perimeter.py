class Solution(object):
    
    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cols = len(grid[0])
        rows = len(grid)
        perimeter = 0


        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1:
                    top = 1 if r == 0 else ( 1 if grid[r-1][c] == 0 else 0 ) 
                    right = 1 if c+1 == cols else ( 1 if grid[r][c+1] == 0 else 0 )
                    left = 1 if c == 0 else ( 1 if grid[r][c-1] == 0 else 0 )
                    below = 1 if r+1 == rows else ( 1 if grid[r+1][c] == 0 else 0 )
                    perimeter += (top + right + left + below)
        return perimeter

        # find a land and recursively expands up to its borders
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.cols = len(grid[0])
        self.rows = len(grid)
        self.grid = grid
        self.visited = set()

        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if grid[r][c] == 1:
                    # top = self.check_perimeter(r, c, top=True)
                    # right = self.check_perimeter(r, c, right=True)
                    # left = self.check_perimeter(r, c, left=True)
                    # below = self.check_perimeter(r, c, below=True)
                    # return top + right + left + below
                    return self.check_perimeter(r,c)
        return 0

    def check_perimeter(self, r, c, top=False, right=False, left=False, below=False):

        # print (r,c)


        if (r,c) in self.visited or r < 0 or r == self.rows or c < 0 or c == self.cols:
            return 0

        if self.grid[r][c] == 0:
            return 1

        self.visited.add((r,c))

        # if (top and (r <= 0 or self.grid[r-1][c] == 0)) or\
        #     (right and (c >= self.cols-1 or self.grid[r][c+1] == 0)) or\
        #     (left and (c <= 0 or self.grid[r][c-1] == 0)) or\
        #     (below and (r >= self.rows-1 or self.grid[r+1][c] == 0)):
        #         return 1

        # return self.check_perimeter(r-1, c, top=True)\
        #         + self.check_perimeter(r, c+1, right=True)\
        #         + self.check_perimeter(r, c-1, left=True)\
        #         + self.check_perimeter(r+1, c, below=True)

        perimeter = 0
        if r == 0:
            perimeter += 1
        if c == self.cols - 1:
            perimeter += 1
        if c == 0:
            perimeter += 1
        if r == self.rows - 1:
            perimeter += 1
        return perimeter + self.check_perimeter(r-1, c)\
                         + self.check_perimeter(r, c+1)\
                         + self.check_perimeter(r, c-1)\
                         + self.check_perimeter(r+1, c)
 
            
            
        # if top:
        #     return self.check_perimeter(r-1, c, top=True)\
        #         + self.check_perimeter(r, c, right=True)\
        #         + self.check_perimeter(r, c, left=True)
        # elif below: 
        #     return self.check_perimeter(r, c, right=True)\
        #         + self.check_perimeter(r, c, left=True)\
        #         + self.check_perimeter(r+1, c, below=True)
        # elif left:
        #     return self.check_perimeter(r-1, c, top=True)\
        #         + self.check_perimeter(r, c, left=True)\
        #         + self.check_perimeter(r, c, below=True)
        # elif right:
        #     return self.check_perimeter(r, c, top=True)\
        #         + self.check_perimeter(r, c+1, right=True)\
        #         + self.check_perimeter(r, c, below=True)
        # else:
        #     return self.check_perimeter(r-1, c, top=True)\
        #         + self.check_perimeter(r, c+1, right=True)\
        #         + self.check_perimeter(r, c-1, left=True)\
        #         + self.check_perimeter(r+1, c, below=True)
 


s = Solution()
print (s.islandPerimeter([[1]]))
print (s.islandPerimeter([[1,0]]))
print (s.islandPerimeter([[1,1]]))
print (s.islandPerimeter([[1,1,1]]))
print (s.islandPerimeter([[1],[1]]))
print (s.islandPerimeter([[1],[0]]))
print (s.islandPerimeter([[0],[1]]))
print (s.islandPerimeter([[1,1],[1,1]]))
print (s.islandPerimeter( [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] ))