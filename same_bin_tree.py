# https://leetcode.com/problems/same-tree/
from invert_bin_tree import build_tree_from_arr

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def same_bin_trees(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        elif tree1 and tree2 and tree1.val == tree2.val:
            left = self.same_bin_trees(tree1.left, tree2.left)
            right = self.same_bin_trees(tree1.right, tree2.right)
            return left and right
        else:
            return False

s  = Solution()
p, q = [1,2,3], [1,2,3]
tree1 = build_tree_from_arr(p, 0)
tree2 = build_tree_from_arr(q, 0)
print (s.same_bin_trees(tree1, tree2))

p, q = [1,2], [1,None,2]
tree1 = build_tree_from_arr(p, 0)
tree2 = build_tree_from_arr(q, 0)
print (s.same_bin_trees(tree1, tree2))

p, q = [1,2,1], [1,1,2]
tree1 = build_tree_from_arr(p, 0)
tree2 = build_tree_from_arr(q, 0)
print (s.same_bin_trees(tree1, tree2))

