# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def traverse_inorder(self, root, ll):
        if root is None:
            return
        self.traverse_inorder( root.left, ll )
        ll.append( root.val )
        self.traverse_inorder( root.right, ll )
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result_l = []
        self.traverse_inorder(root, result_l)
        return result_l