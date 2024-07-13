# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Estava com a binary search o tempo todo na cabeça mas tem uma jeito similar e ótimo de resolver que não
# necessariamente é uma binary search.
# https://www.youtube.com/watch?v=9ZbB397jU4k

# Minha solução "descente" com binsearch

class Solution:

    def bin_search(self, target, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target == row[len(row)-1]:
                return True
            if target < row[len(row)-1]:
                if self.bin_search(target, row):
                    return True
        return False