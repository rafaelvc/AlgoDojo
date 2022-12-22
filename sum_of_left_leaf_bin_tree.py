from invert_bin_tree import build_tree_from_arr

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    # def sumOfLeftLeaves1(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     if root.left and root.left.left is None and root.left.right is None:
    #         return root.left.val + self.sumOfLeftLeaves(root.right)
    #     return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [ root ]
        sum_lleaf = 0
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                continue
            if node.left and node.left.left is None and node.left.right is None:
                sum_lleaf += node.left.val
                queue.append(node.right)
            else:
                queue.append(node.left)
                queue.append(node.right)
        return sum_lleaf

    
root = [3,9,20,None,None,15,7]
tree = build_tree_from_arr(root, 0)
print (Solution().sumOfLeftLeaves(tree))

root = [1]
tree = build_tree_from_arr(root, 0)
print (Solution().sumOfLeftLeaves(tree))
          
root = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
tree = build_tree_from_arr(root, 0)
print (Solution().sumOfLeftLeaves(tree)) #5
