from invert_bin_tree import build_tree_from_arr

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def level_order_traverse(self, root, arr_result, next_level):
        if root is None:
            return
        if len(arr_result) == next_level:
            arr_result.append([root.val])
        else:
            arr_result[next_level].append(root.val)
        self.level_order_traverse(root.left, arr_result, next_level + 1)
        self.level_order_traverse(root.right, arr_result, next_level + 1)

    def levelOrder(self, root: TreeNode):
        result_arr = []
        self.level_order_traverse(root, result_arr, 0)
        return result_arr

# memory limit:
# [9,14,14,74,null,null,74,null,12,12,null,63,null,null,63,-8,null,null,-8,-53,null,null,-53,null,-96,-96,null,-65,null,null,-65,98,null,null,98,50,null,null,50,null,91,91,null,41,-30,-30,41,null,86,null,-36,-36,null,86,null,-78,null,9,null,null,9,null,-78,47,null,48,-79,-79,48,null,47,-100,-86,null,47,null,67,67,null,47,null,-86,-100,-28,11,null,56,null,30,null,64,64,null,30,null,56,null,11,-28,43,54,null,-50,44,-58,63,null,null,-43,-43,null,null,63,-58,44,-50,null,54,43]

root = [1,2,2,3,3,3,3]
tree = build_tree_from_arr(root, 0)
print (Solution().levelOrder(tree))

root = [3,9,20,None,None,15,7]
tree = build_tree_from_arr(root, 0)
print (Solution().levelOrder(tree))