# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
import random
import cProfile, pstats

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

class LinkedList:

    def __init__(self, head=None):

        self.head = head
        self.counter = 0
        self.sum = 0
        if self.head:
            self.counter += 1
            self.sum = head.value

    def __iter__(self):

        node = self.head
        while node != None:
            yield node.value
            node = node.next
        #raise StopIteration

    def __repr__(self):

        return " -> ".join([str(node) for node in self])

    def pop(self):

        if self.head is not None:
            n = self.head 
            # self.sum -= self.head.value
            self.head = self.head.next
            self.counter -= 1
            return n 
        return None
    

    def from_list_to_linkedlist(arr):
        ll = LinkedList()
        last = Node( arr[0] )
        ll.fifo_insert( last )
        for x in arr[1:]:
            node = Node(x)
            ll.fifo_insert( node, last=last )
            last = node
        return ll

    def fifo_insert(self, node, last=None):

        if self.head is None:
            self.head = node
            return node
        if last:
            last.next = node
        else:
            n = self.head 
            while n.next:
                n = n.next
            n.next = node    
        return node

    def lifo_insert(self, node):

        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def sort_insert(self, node, asc=True):
        # ASC == TRUE inserts in ascending order 1,2,3...
        # ASC == FALSE inserts in descending order 3,2,1...
        # The sorted(reversed=True) implementation seems to sort in asc order 
        # and then it reverts the list using a two pointers approach
        if asc:
            head_check = lambda x, y : x <= y
            body_check = lambda x, y : x >= y
        else:
            head_check = lambda x, y : x >= y
            body_check = lambda x, y : x <= y

        self.counter += 1
        self.sum += node.value
        if self.head is None:
            self.head = node
            return
        # if node.value <= self.head.value: (ASC)
        # if node.value >= self.head.value: (DESC)
        if head_check(node.value, self.head.value):
            node.next = self.head
            self.head = node
            return 
        n = self.head
        prev = n
        # while n != None and node.value >= n.value: (ASC)
        # while n != None and node.value <= n.value: (DESC)
        while n != None and body_check(node.value, n.value):
            prev = n
            n = n.next
        node.next = n
        prev.next = node

# Linked list with Insert Asc/Desc Sort tests
# raninput = [ random.randint(0,10) for r in 10 * [0]  ]
# linkedlist = LinkedList()
# print (raninput)
# for x in raninput:
#     linkedlist.sort_insert( Node(x), asc = False)
# print (linkedlist)
# linkedlist.pop()
# print (linkedlist)
# linkedlist.pop()

# raninput = [ random.randint(0,10) for r in 10 * [0]  ]
# print (raninput)
# linkedlist = LinkedList.from_list_to_linkedlist(raninput)
# print (linkedlist)

def mean_after_removing_some(arr, percent=5):

    some = int(len(arr) * (percent / 100)) # %5 percent
    total_sum = arr[0] + arr[1]
    largest = LinkedList( Node(max(arr[0], arr[1])) )
    smallest = LinkedList( Node(min(arr[0], arr[1])) )
    # print ( '{} : {}'.format( smallest, largest ) )
    for x in arr[2:]:
        if x >= largest.head.value:
            if largest.counter == some:
                n = largest.pop()
                if n and smallest.counter < some:
                    smallest.sort_insert(n , asc=False)
                elif n and smallest.counter == some and n.value <= smallest.head.value:
                    smallest.pop()
                    smallest.sort_insert(n , asc=False)
            largest.sort_insert( Node(x) )
        elif x <= smallest.head.value:
            if smallest.counter == some:
                n = smallest.pop()
                if n and largest.counter < some:
                    largest.sort_insert( n )
                elif n and largest.counter == some and n.value >= largest.head.value:
                    largest.pop()
                    largest.sort_insert(n)
            smallest.sort_insert( Node(x), asc=False )
        # print ( '{} : {}'.format( smallest, largest) )
        # print ( '{} : {}'.format( largest, largest.sum) )
        total_sum += x
    # print ( '{} : {}'.format( smallest, largest ) )
    return (total_sum - (largest.sum + smallest.sum)) / (len(arr) - (some*2))


def mean_after_removing_some_with_sort(arr, percent=5):
    some = int(len(arr) * (percent / 100)) # %5 percent
    arr = sorted(arr)
    # print ( '{} : {}'. format(arr[:some], arr[-some:]) )
    return (sum(arr) - (sum(arr[:some])+ sum(arr[-some:]))) / (len(arr) - (some*2))

# arr = list ( reversed( [1,2,3,4,5,6] ) )
# arr = [1,2,3,4,5,6]
# print (mean_after_removing_some(arr, 40))


# def mean_after_removing_some(arr, percent=5):
# 
#     # Array is multiple of 20
#     # if len(arr) % 20 != 0:
#     #    return 0
#     smallest_max = max( arr[0], arr[1] ) 
#     next_smallest_max = smallest_max + 1
#     largest_min = min( arr[0], arr[1] )
#     next_largest_min = largest_min 
#     # print (smallest_max, largest_min)
#     smallest_sum = smallest_max
#     largest_sum = largest_min
#     smallest_counter = 1
#     largest_counter = 1
#     smallest_largets_nr = len(arr) * (percent / 100) # %5 percent
#     total_sum = arr[0] + arr[1]
# 
#     for x in arr[2:]:
#         if x <= largest_min:
# 
#             if largest_counter == smallest_largets_nr:
#                 largest_sum -= largest_min
#                 # largest_min = next_largest_min
#                 largest_min = x
#                 # if x > next_largest_min or ( next_largest_min == -1 and x != next_largest_min):
#                 #    next_largest_min = x
#             else:
#                 largest_counter += 1
#             largest_sum += x
# 
#         elif x >= smallest_max: 
# 
#             if smallest_counter == smallest_largets_nr:
#                 smallest_sum -= smallest_max
#                 # smallest_max = next_smallest_max
#                 smallest_max = x
#             else:
#                 # if x < next_smallest_max or ( next_smallest_max == -1 and x != next_smallest_max):
#                 #    next_smallest_max = x
#                 smallest_counter += 1
#             smallest_sum += x
#         total_sum += x
# 
#     # print (total_sum, smallest_sum, largest_sum)
# 
#     return (total_sum - (smallest_sum + largest_sum)) / (len(arr) - (smallest_largets_nr*2))
# 
# 

# 
# arr = [1,2,2,2,3]
# print (mean_after_removing_some(arr, 20))
#  
# arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
# # # print (mean_after_removing_some_with_sort(arr))
# print (mean_after_removing_some(arr))
# # 
# #  
# arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
# # # print (mean_after_removing_some_with_sort(arr))
# print (mean_after_removing_some(arr))
#  
# arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# # print (mean_after_removing_some_with_sort(arr))
# print (mean_after_removing_some(arr))


# arr = [random.randint(0,10) for r in 1000000 * [0]]
# def profile1():
# 
#     # arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
#     mean_after_removing_some(arr, 10)
# 
# def profile2():
#     # arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
#     mean_after_removing_some_with_sort(arr, 10)
# # 
# # cProfile.run('profile1()')
# # print ('..............')
# # cProfile.run('profile2()')
# 
# profiler = cProfile.Profile()
# 
# # profiler.enable()
# # profile1()    
# # profiler.disable()
# # stats = pstats.Stats(profiler).sort_stats('ncalls')
# # stats.print_stats()
# 
# profiler.enable()
# profile2()    
# profiler.disable()
# stats = pstats.Stats(profiler).sort_stats('ncalls')
# stats.print_stats()