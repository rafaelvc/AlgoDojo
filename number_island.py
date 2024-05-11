from typing import List, Tuple
from collections import deque
import multiprocessing as mp
from ctypes import c_int
import os

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.visited = set()
        island_counter = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.navigateIslandStacked(row, col):
                    island_counter += 1
        return island_counter 

    def numIslands2(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.visited = set()
        island_counter = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.navigateIsland(row, col)
                    island_counter += 1
        return island_counter 

    def navigateIsland(self, row, col):
        if (row, col) in self.visited:
            return
        self.visited.add((row, col))
        if self.grid[row][col] == "0":
            return
        # go to right 
        right = col + 1 
        if right < self.cols:
            self.navigateIsland(row, right)
        # go to down
        down = row + 1
        if down < self.rows:
            self.navigateIsland(down, col)
        # go to left
        left = col - 1
        if left >= 0:
            self.navigateIsland(row, left)
        # go to up
        up = row - 1 
        if up >= 0:
            self.navigateIsland(up, col)
    
    def numIslandsStacked(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.visited = set()
        island_counter = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.navigateIslandStacked(row, col):
                    island_counter += 1
        return island_counter 

    def navigateIslandStacked2(self, row, col):
        if self.grid[row][col] == "0" or (row, col) in self.visited:
            return False
        land_stack = deque()
        land_stack.append( (row,col) )
        while len(land_stack) > 0:
            (row, col) = land_stack.pop()
            self.visited.add((row, col))
            right = col + 1  # go to right
            if right < self.cols and self.canStep(row, right):
                land_stack.append( (row, right) )
            down = row + 1 # go to down
            if down < self.rows and self.canStep(down, col):
                land_stack.append( (down, col) )
            left = col - 1 # go to left
            if left >= 0 and self.canStep(row, left):
                land_stack.append( (row, left) )
            up = row - 1 # go to up
            if up >= 0 and self.canStep(up, col):
                land_stack.append( (up, col) )
        return True

    def navigateIslandStacked(self, row, col):
        if self.grid[row][col] == "0" or (row, col) in self.visited:
            return False
        land_stack = deque()
        land_stack.append( (row,col) )
        while len(land_stack) > 0:
            (row, col) = land_stack.pop()
            self.visited.add((row, col))
            self.stepInLand(row, col, land_stack)
        return True

    def stepInLand(self, row, col, land_stack):
        self.stepRight(row, col, land_stack)
        self.stepDown(row, col, land_stack)
        self.stepLeft(row, col, land_stack)
        self.stepUp(row, col, land_stack)

    def stepUp(self, row, col, land_stack):
        row -= 1
        if row >= 0 and self.canStep(row, col):
            land_stack.append((row, col))

    def stepLeft(self, row, col, land_stack):
        col =- 1
        if col >= 0 and self.canStep(row, col):
            land_stack.append((row, col))

    def stepDown(self, row, col, land_stack):
        row += 1
        if row < self.rows and self.canStep(row, col):
            land_stack.append((row, col))

    def stepRight(self, row, col, land_stack):
        col += 1
        if col < self.cols and self.canStep(row, col):
            land_stack.append((row, col))
 
    def canStep(self, row, col):
        return self.grid[row][col] == "1" and (row, col) not in self.visited
    
    #(start row, end row, start col, end col)
    def getSubGrid(self, area : int) -> Tuple[int, int, int, int]:
        if area == 1:
            return (0, self.rows // 2, 0, self.cols // 2,)
        elif area == 2:
            return (0, self.rows // 2, self.cols // 2, self.cols)
        elif area == 3:
            return (self.rows // 2, self.rows, 0, self.cols // 2)
        elif area == 4:
            return (self.rows // 2, self.rows, self.cols // 2, self.cols)

    def navigateSubIslandStacked(self, row, col):
        if (row, col) in self.visited or self.grid[row][col] == "0":
            return False
        land_stack = deque()
        land_stack.append( (row,col) )
        while len(land_stack) > 0:
            (row, col) = land_stack.pop()
            self.visited.add((row, col))
            right = col + 1  # go to right
            if right < self.col_end and self.canStep(row, right):
                land_stack.append( (row, right) )
                self.check_border_land(row, right)
            down = row + 1 # go to down
            if down < self.row_end and self.canStep(down, col):
                land_stack.append( (down, col) )
                self.check_border_land(down, col)
            left = col - 1 # go to left
            if left >= self.col_start and self.canStep(row, left):
                land_stack.append( (row, left) )
                self.check_border_land(row, left)
            up = row - 1 # go to up
            if up >= self.row_start and self.canStep(up, col):
                land_stack.append( (up, col) )
                self.check_border_land(up, col)
        return True
    
    def check_border_land(self, row, col):
        pass

    def post_process_borderlands(sef):
        # The idea is merge subisland from different grid areas 
        # are neighboors. So we decrement the island couter
        # by one each two subislands are 'merged'.
        pass

    def numIslands(self, grid: List[List[str]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        sub_island_counter = 0
        self.visited = set()

        # For checking A/B neighboors
        self.right_borderland_A = mp.Array(c_int, self.rows // 2)
        self.right_borderland_A.len = 0 # monkey patch a len attr, I am not sure it is possible Array is a shared mem object.
        self.left_borderland_B = mp.Array(c_int, self.rows // 2)
        self.left_borderland_B.len = 0

        # For checking A/C neighboors
        self.down_borderland_A = mp.Array(c_int, self.cols // 2)
        self.up_borderland_C = mp.Array(c_int, self.cols // 2)

        # For checking C/D neighboors
        self.right_borderland_B = mp.Array(c_int, self.rows // 2)
        self.left_borderland_D = mp.Array(c_int, self.rows // 2)

        # For checking D/B neighboors
        self.down_borderland_B = mp.Array(c_int, self.cols // 2)
        self.up_borderland_D = mp.Array(c_int, self.cols // 2)


        with mp.Pool(processes=4) as pool:
           sub_island_counter = sum(pool.map(self.numIslandsParallel, [1,2,3,4]))
        return sub_island_counter

        # Lands are neighboors in subareas are part of same island
        # Merge subislands 1 and 2
           
        # Merge subislands 1 and 3 
           
        # Merge subislands 3 and 4
           
        # Merge subislands 2 and 4


    def numIslandsParallel(self, area: int) -> int:
        # Each worker has its own copy of self
        self.row_start, self.row_end, self.col_start, self.col_end = self.getSubGrid(area)
        sub_island_counter = 0
        for row in range(self.row_start, self.row_end):
            for col in range(self.col_start, self.col_end):
                if self.navigateSubIslandStacked(row, col):
                    sub_island_counter += 1
        return sub_island_counter 




# grid = [["1"]]
# grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# print (Solution().numIslands(grid))
print (Solution().numIslandsStacked(grid))
