from invert_bin_tree import build_tree_from_arr
from math import pow

def breadth_first_traversal(root, f):

    queue = []
    queue.append( root )
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            continue 
        f (node.val, end = " ")
        queue.append( node.left )
        queue.append( node.right )

def breadth_first_traversal_zig_right(root, f):
    queue = []
    queue.append( root )
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            continue 
        f (node.val, end = " ")
        queue.append( node.right )
        queue.append( node.left )

def breadth_first_traversal_(root, f):
    queue = []
    queue.append( root )
    side_left = True
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            continue 
        f (node.val, end = " ")
        if side_left: 
            queue.append( node.left )
            queue.append( node.right )
        else:
            queue.append( node.right )
            queue.append( node.left )
        side_left = not side_left
           

def height(node):
    if node is None:
        return 0
    # Compute the height of each subtree
    lheight = height(node.left)
    rheight = height(node.right)
    # Use the larger one
    if lheight > rheight:
        return lheight+1
    return rheight+1

# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


def breadth_first_traversal_level_print(root):
    queue = []
    queue.append( root )
    level = 0
    level_counter = 1
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            continue 
        if level_counter == 0:
            level += 1
            level_counter =int (pow(2, level))
            print (" ")
        level_counter -= 1
        print (node.val, end = " ")
        queue.append( node.left )
        queue.append( node.right )

def breadth_first_traversal_level_list(root):
    if root is None:
        return []
    queue = []
    queue.append( root )
    level = 0
    level_counter = 1
    arr = [[]]
    while True:
        node = queue.pop(0)
        if node:
            arr[level].append(node.val)
            queue.append(node.left)
            queue.append(node.right)
            has_node_level = True
        else:
            queue.append(None)
            queue.append(None)
        level_counter -= 1
        if level_counter == 0:
            if not has_node_level: # We hit the last level
                if arr[len(arr)-1] == []:
                    return arr[:-1]
                return arr
            has_node_level = False
            level += 1
            level_counter = int(pow(2, level))
            arr.append([])

def breadth_first_traversal_level_list2(root):
    if root is None:
        return []
    queue = []
    queue.append( root )
    level = 0
    next_level_nodes = 1
    level_counter = 1
    arr = [[]]
    null_nodes = 0
    while len(queue) > 0:
        node = queue.pop(0)
        arr[level].append(node.val)
        level_counter -= 1
        if node.left:
            queue.append(node.left)
        else:
            null_nodes += 1
        if node.right:
            queue.append(node.right)
        else:
            null_nodes += 1
        if level_counter == 0:
            level_counter = (next_level_nodes * 2) - null_nodes
            if level_counter == 0:
                return arr
            level += 1
            null_nodes *= 2
            next_level_nodes *= 2
            arr.append([])
    return arr

            
# root = [1,2,2,3,4,5,6]
# tree = build_tree_from_arr( root, 0 )
# breadth_first_traversal( tree, print )

root = [3,9,20,None,None,15,7]
tree = build_tree_from_arr( root, 0 )
print (breadth_first_traversal_level_list2( tree ))
 
# root = [1,2,None,3,None,4,None,5] Invalid array!
root = [1,2,None,3,None,None,None,4,None,None,None,None,None,None,None,5]
tree = build_tree_from_arr( root, 0 )
# breadth_first_traversal(tree, print)
print (breadth_first_traversal_level_list2( tree ))

root = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tree = build_tree_from_arr( root, 0 )
print (breadth_first_traversal_level_list2( tree ))

root = [1,2]
tree = build_tree_from_arr( root, 0 )
print (breadth_first_traversal_level_list2( tree ))
 
root = [1,2,3]
tree = build_tree_from_arr( root, 0 )
print (breadth_first_traversal_level_list2( tree ))

# Run out of time expection on leet code: breadth_first_traversal_level_list
root = [69,73,68,18,20,18,39,7,-3,13,-1,42,5,93,70,63,17,None,91,-4,30,None,-1,64,-4,16,49,48,78,51,43,92,45,None,53,9,36,80,-6,58,78,None,None,41,81,89,67,71,None,25,None,82,54,28,14,61,57,35,5,83,9,18,None,-9,-9,50,92,93,None,0,80,62,1,28,29,27,89,21,None,85,-9,None,56,56,-9,None,None,43,None,29,97,-7,None,35,25,90,67,53,18,61,7,23,81,37,19,26,2,0,19,None,None,77,37,-2,None,49,39,28,1,37,11,87,83,68,55,53,33,-2,22,7,52,None,14,None,18,50,97,-8,-7,None,21,59,72,27,None,64,None,None,47,None,None,38,46,None,None,99,None,None,48,13,85,78,7,64,43,59,71,11,37,12,37,50,2,None,None,89,87,None,78,97,None,31,86,37,96,34,38,6,36,None,None,99,63,None,12,None,82,None,81,70,19,None,81,32,None,None,None,None,79,10,None,91,48,-3,94,65,None,20,26,96,21,92,91,None,89,9,74,None,None,96,None,64,67,50,96,None,None,None,None,None,None,40,78,None,27,3,17,None,None,2,45,None,None,None,None,None,13,None,None,17,45,69,30,None,None,43,None,4,13,-6,66,6,None,16,48,55,98,69,57,None,5,9,65,-9,55,2,None,None,None,None,None,None,68,None,None,None,5,61,51,None,None,32,43,None,35,20,None,-7,38,30,1,80,None,None,42,86,42,None,None,None,None,47,None,None,None,62,29,-9,83,60,71,48,None,24,None,76,6,65,18,95,29,11,None,38,None,None,None,None,21,3,6,23,36,None,45,None,34,None,None,None,None,None,None,41,None,57,13,18,92,43,83,None,None,None,None,None,None,None,2,-4,97,None,93,None,62,None,None,48,18,71,92,53,89,None,None,None,95,None,16,None,None,None,83,87,5,None,None,3,-8,-4,65,None,None,None,22,None,31,None,None,None,63,None,None,62,None,57,12,85,45,23,55,None,None,None,81,83,23,None,3,None,83,None,-4,None,None,None,None,None,64,None,15,50,57,None,None,None,4,None,None,None,29,None,None,87,None,22,92,None,None,67,90,None,93,47,46,None,None,None,28,72,18,59,25,3,74,None,None,None,-5,28,-1,61,15,None,None,None,None,79,None,16,None,None,59,47,-7,98,31,50,None,None,None,None,19,None,93,None,22,None,None,-5,40,None,None,None,75,30,None,7,53,76,None,None,None,None,None,68,19,None,63,41,91,None,43,None,49,None,None,None,None,None,46,None,None,87,74,49,1,21,62,6,34,77,None,None,None,None,None,None,-9,61,None,None,None,7,None,45,None,None,63,None,None,7,None,None,16,86,None,None,63,None,61,72,None,13,None,24,91,None,None,59,None,None,48,14,77,None,None,None,None,92,None,None,None,None,None,None,84,None,None,76,82,63,84,84,94,None,None,None,None,None,47,40,None,None,None,None,75,20,None,None,None,-9,None,None,24,74,None,51,None,None,91,None,83,17,None,None,None,42,49,88,57,85,1,None,94,None,28,36,78,None,53,None,27,25,46,97,58,None,None,None,None,None,None,None,None,12,33,None,None,6,None,None,None,87,None,None,None,None,None,None,None,9,None,83,None,None,None,90,11,None,61,None,89,None,46,None,86,81,None,None,None,None,None,None,None,53,None,None,59,None,None,None,None,None,None,None,29,None,47,97,0,None,None,None,None,9,None,17,None,91,45,9,61,21,None,None,64,None,69,None,44,None,None,None,None,12,None,2,-8,88,None,None,None,None,None,-8,None,93,None,None,None,86,None,None,97,None,None,None,None,72,None,None,None,None,None,50,None,None,None,None,None,47,70,None,62,None,-3,-5,59,15,None,-3,37,None,None,None,None,20,-2,None,8,90,None,None,None,61,None,None,None,None,None,None,None,15,12,95,None,None,73,11,76,76,49,None,None,51,None,None,None,None,None,None,None,None,None,None,None,None,None,42,None,None,-9,None,None,None,None,None,None,None,None,80,None,None,70,31,78,98,None,None,None,None,None,None,None,None,None,None,None,None,7,None,None,None,None,57,None,None,None,None,-3,None,None,-7,None,31,42,None,None,None,None,62,17,7,None,None,63,None,None,None,None,83,51,None,76,77,None,None,40,None,None,95,None,27,55,61,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,95,None,93,19,None,37,None,73,None,None,None,None,None,75,None,None,None,None,None,22,None,None,None,None,None,-7,99,None,None,None,None,None,94,63,None,None,None,None,None,None,None,39,77,None,-2,15,None,69,33,9,None,None,None,None,None,None,None,None,None,42,None,None,None,69,35,None,36,None,11,None,None,None,52,None,None,None,None,None,None,None,51,50,None,None,None,None,None,None,30,None,None,None,None,None,63,None,None,None,None,None,None,56,28]
tree = build_tree_from_arr( root, 0 )
print (breadth_first_traversal_level_list2( tree ))
