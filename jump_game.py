
from typing import List
from collections import deque

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        pos = 0
        stack = deque( [(nums[pos], pos)] )
        while len(stack) > 0:
            hope, pos = stack.pop()
            if hope == 0:
                continue
            if pos + hope >= len(nums) - 1:
                return True
            if nums[pos + hope] == 0:
                hope -= 1
                stack.append( (hope, pos) )
            else:
                stack.append( (hope-1, pos) )
                pos += hope
                stack.append( (nums[pos], pos) )
        return False

    def canJump2(self, nums: List[int]) -> bool:
        if len(nums) == 1: 
            return True
        stack = deque( [ (nums[0], 0) ] )
        unjumpable_pos = set()
        while len(stack) > 0:
            jump, pos = stack.pop()
            if jump == 0:
                unjumpable_pos.add( pos )
                continue
            if pos + jump >= len(nums) - 1:
                return True
            stack.append( (jump-1, pos) )
            if nums[pos + jump] == 0:
                unjumpable_pos.add(pos + jump)
            else:
                pos += jump
                if pos not in unjumpable_pos:
                    stack.append( (nums[pos], pos) )
        return False

    def canJump3(self, nums: List[int]) -> bool:
        if len(nums) == 1: 
            return True
        if nums[0] == 0:
            return False
        zeros_pos = set()
        pos = len(nums)-1
        for jump in reversed(nums[:-1]):
            if jump == 0:
                zeros_pos.add(pos)    
            elif (pos + jump) in zeros_pos:
                zeros_pos.add(pos)    
            pos -= 1
        return not (nums[0] in zeros_pos)

    # [3,0,8,2,0,0,1] # Recursive solution gives time limit
    def canJump4(self, nums: List[int]) -> bool:
        self.nums = nums
        return self.Jump(0)

    def Jump(self, cur_pos=0) -> bool:
        if cur_pos >= len(self.nums)-1: 
            return True
        if self.nums[cur_pos] == 0:
            return False
        jump = cur_pos + self.nums[cur_pos] 
        if jump >= len(self.nums)-1: 
            return True
        # if self.nums[jump] > 0:
        #    return False or self.Jump(jump)
        result = False
        next_jump = self.nums[cur_pos]
        while next_jump > 0:
            if self.nums[cur_pos + next_jump] == 0:
                next_jump -= 1
                continue
            result = result or self.Jump(cur_pos + next_jump)
            next_jump -= 1
        return result


# nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
# nums = [2,5,0,0]
# nums = [0,1]
# nums = [1,0,2]
# nums = [2,0,0]

s = Solution()
print (s.canJump2(nums))



def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    last_ix = 0
    for i, n in enumerate(nums):
        if n == 0:
            



 