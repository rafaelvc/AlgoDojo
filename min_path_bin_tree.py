# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional
from in_order_bin_tree import TreeNode
from invert_bin_tree import build_tree_from_arr
# import pdb

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 and right > 0:
            return 1 + right
        elif right == 0 and left > 0:
            return 1 + left
        return 1 + (left if left <= right else right)


print (Solution().minDepth(build_tree_from_arr([3,9,20,None,None,15,7], 0)))
# pdb.set_trace()
# a = build_tree_from_arr([2,None,3,None,4,None,5,None,6], 0)
print (Solution().minDepth(build_tree_from_arr([2,None,3,None,4,None,5,None,6], 0)))
# REVIEW: build_tree_from_arr expects [2,None,3,None,None,None,4...] instead