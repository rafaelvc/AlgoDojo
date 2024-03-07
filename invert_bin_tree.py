# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
 
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         pass

def traverse_tree_arr( arr, root ):
    # leaf
    if (root >= len(arr)):
        return None
    left = (root * 2) + 1
    right = left + 1
    # print (arr[root]) # pre order
    traverse_tree_arr( arr, left )
    # print (arr[root]) # in order
    traverse_tree_arr( arr, right )
    print (arr[root]) # pos order

def build_tree_from_arr( arr, root ):
    # leaf
    if root >= len(arr) or arr[root] is None:
        return
    left = (root * 2) + 1
    right = left + 1
    left_root = build_tree_from_arr(arr, left)
    right_root = build_tree_from_arr(arr, right)
    return TreeNode(arr[root], left_root, right_root)

def traverse_tree( root ):
    # leaf
    if root is None:
        return
    print (root.val)
    traverse_tree( root.left )
    traverse_tree( root.right )

def inverse_tree( root ):
    # leaf
    if root is None:
        return
    inverse_tree( root.left )
    inverse_tree( root.right )
    root.left, root.right = root.right, root.left


# root = [1,2,None,3,None,None,None,4]
# root = [1,2,None,3,None,4,None,5]
# tree = build_tree_from_arr( root, 0 )
# traverse_tree(tree)

tree = [4,2,7,1,3,6,9]
traverse_tree_arr(tree, 0)
# #  print ('---')
# root = build_tree_from_arr(tree, 0)
# inverse_tree(root)
# traverse_tree(root)
