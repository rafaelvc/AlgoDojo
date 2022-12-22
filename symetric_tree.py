from invert_bin_tree import build_tree_from_arr, traverse_tree
from invert_bin_tree import TreeNode
from collections import deque
import cProfile, pstats

class Solution:

    def last_level(self, nodes):
        for n in nodes:
            if n is not None:
                return False 
        return True

    def check_simetric_level(self, nodes):
        l, r = 0, len(nodes)-1
        while l <= r:
            if nodes[l] == None and nodes[r] == None:
                l += 1
                r -= 1
                continue
            elif (nodes[l] == None or nodes[r] == None) or\
                 (nodes[l].val != nodes[r].val):
                return False
            l += 1
            r -= 1
        return True

    def build_level_from_prev(self, nodes):
        if nodes == []:
            return []
        node = nodes[0]
        if node == None:
            l = [None, None]
        else:
            l = [node.left, node.right]
        return l + self.build_level_from_prev(nodes[1:])

# memory limit:
# [9,14,14,74,null,null,74,null,12,12,null,63,null,null,63,-8,null,null,-8,-53,null,null,-53,null,-96,-96,null,-65,null,null,-65,98,null,null,98,50,null,null,50,null,91,91,null,41,-30,-30,41,null,86,null,-36,-36,null,86,null,-78,null,9,null,null,9,null,-78,47,null,48,-79,-79,48,null,47,-100,-86,null,47,null,67,67,null,47,null,-86,-100,-28,11,null,56,null,30,null,64,64,null,30,null,56,null,11,-28,43,54,null,-50,44,-58,63,null,null,-43,-43,null,null,63,-58,44,-50,null,54,43]
    def isSymetricMy(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        nodes_level = [root.left, root.right]
        while not self.last_level(nodes_level):
#            print ([n.val for n in nodes_level])
            if not self.check_simetric_level(nodes_level):
                return False
            nodes_level = self.build_level_from_prev(nodes_level)
        return True

    def isSymetricIter(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = deque()
        q.append (root.left)
        q.append (root.right)
        while len(q) > 0:
            root1 = q.popleft()
            root2 = q.popleft()
            if root1 is None and root2 is None:
                continue
            elif root1 is None or root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            q.append (root1.left) 
            q.append (root2.right) 
            q.append (root1.right) 
            q.append (root2.left)
        return True

    def isSymetricRec(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and self.isMirror (root1.left, root2.right) and\
                                          self.isMirror (root1.right, root2.left)
        

profiler = cProfile.Profile()

# root = [1,2,2,3,4,4,3]
# tree = build_tree_from_arr(root, 0)
# profiler.enable()
# print (Solution().isSymetricRec(tree))
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# profiler.enable()
# print (Solution().isSymetricMy(tree))
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()

# root = [1,2,2,None,3,3,None]
# tree = build_tree_from_arr(root, 0)
# print (Solution().isSymmetric(tree))

# root = [1,2,2,None,3,None,3]
# tree = build_tree_from_arr(root, 0)
# traverse_tree(tree)

# profiler.enable()
# print (Solution().isSymetricRec(tree))
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# profiler.enable()
# print (Solution().isSymetricMy(tree))
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()

# root = [1,2,2,None,3,3]
root = [9,14,14,74,None,None,74,None,12,12,None,63,None,None,63,-8,None,None,-8,-53,None,None,-53,None,-96,-96,None,-65]#None,None,-65,98,None,None,98,50,None,None,50,None,91,91,None,41,-30]#,-30,41,None,86,None,-36,-36,None,86,None,-78,None,9,None,None,9,None,-78,47,None,48,-79,-79,48,None,47,-100,-86,None,47,None,67,67,None,47,None,-86,-100,-28,11,None,56,None,30,None,64,64,None,30,None,56,None,11,-28,43,54,None,-50,44,-58,63,None,None,-43,-43,None,None,63,-58,44,-50,None,54,43]
tree = build_tree_from_arr(root, 0)
traverse_tree(tree)
# profiler.enable()
# print (Solution().isSymetricRec(tree))
# print (Solution().isSymetricIter(tree))
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# profiler.enable()
# print (Solution().isSymetricMy(tree))
# stats = pstats.Stats(profiler).get_stats_profile()
# print (stats.total_tt)
# profiler.disable()
# print (traverse_tree(tree))



# memory limit:
# [9,14,14,74,null,null,74,null,12,12,null,63,null,null,63,-8,null,null,-8,-53,null,null,-53,null,-96,-96,null,-65,null,null,-65,98,null,null,98,50,null,null,50,null,91,91,null,41,-30,-30,41,null,86,null,-36,-36,null,86,null,-78,null,9,null,null,9,null,-78,47,null,48,-79,-79,48,null,47,-100,-86,null,47,null,67,67,null,47,null,-86,-100,-28,11,null,56,null,30,null,64,64,null,30,null,56,null,11,-28,43,54,null,-50,44,-58,63,null,null,-43,-43,null,null,63,-58,44,-50,null,54,43]