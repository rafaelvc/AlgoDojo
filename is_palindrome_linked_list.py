# Crack coding invertview page 218
# Case the total ammount of the linked list elements 
# is not available it uses a low and fast pointer runner to
# reach the middle position and it stacks list elemens up to there
# and then it compares each element from the stack with the second
# half of the linked list up to the end
# # low fast runner pointer
# arr = [ i for i in range(1,11) ]
# j = 0
# j = 1 
# for i in range(1, len(arr)):
#     print (arr[i-1], arr[j-1]) 
#     if j == len(arr):
#         break
#     j += 2
# Brute force solution for palindrome is to create a reversed list and compare with the original
# if equal it is palindrome

from mean_array_leetcode_1619 import LinkedList, Node

def is_palindrome_linkedlist(ll: LinkedList):
    palin_stack = LinkedList()
    low, fast = ll.head, ll.head
    while fast != None and fast.next != None:
        palin_stack.lifo_insert( Node(low.value) )
        low = low.next
        fast = fast.next.next
    if fast != None:
        low = low.next 
    while low != None:
        n = palin_stack.pop()
        if n.value != low.value:
            return False
        low = low.next
    return True

w = 'a'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'ab'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'aba'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'abba'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'xyzx'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'xyya'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'noon'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))
w = 'level'
ll = LinkedList.from_list_to_linkedlist(w)
print (is_palindrome_linkedlist(ll))