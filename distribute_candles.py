class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        solutions = set()
        total = 0
        for x in range(limit, 0, -1):
            total += 3 
            y = abs(n - x)
            print(x, y, 0)
            if y > limit:
                continue
            z = 0
            while y >= 1:
                total += 3
                y -= 1 
                z += 1
                print(x, y, z)
        return len(solutions)

Solution().distributeCandies(5,2)