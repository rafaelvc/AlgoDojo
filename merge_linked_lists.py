#https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head, tail = None, None
        while list1 != None and list2 != None:
            if list1.val == list2.val:
                node = ListNode(list1.val, ListNode(list2.val))
                list1 = list1.next 
                list2 = list2.next
            elif list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next 
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            if head is None:
                head, tail = node, node
            else:
                tail.next = node
                tail = node
            if tail.next is not None:
                tail = tail.next
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2
        return head

def linked_list_from_arr(arr):
    head = ListNode( arr[0] )
    n = head
    for x in arr[1:]:
        n.next = ListNode(x)
        n = n.next
    return head

def print_list(l):
    while l is not None:
        print(l.val, end=" ")
        l = l.next
    print()

# l1 = linked_list_from_arr( sorted([random.randrange(0,11) for i in range(0,5)]) )
# l2 = linked_list_from_arr( sorted([random.randrange(0,11) for i in range(0,10)]) )
# l3 = Solution().mergeTwoLists(l1, l2)
# print_list (l1)
# print_list (l2)
# print_list( l3 )
