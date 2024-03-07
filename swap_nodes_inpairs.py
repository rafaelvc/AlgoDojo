
from typing import Optional
from merge_linked_lists import linked_list_from_arr, print_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        x = head
        y = head.next
        head = y
        p = None
        while x != None and y != None:
            x.next = y.next
            y.next = x
            if p != None:
                p.next = y
            p = x
            x = x.next 
            if x is None:
                break
            y = x.next
        return head

arr = linked_list_from_arr([1,2,3,4])
print_list( Solution().swapPairs(arr) )

# 5 2 4 3 2 6 2
arr = linked_list_from_arr([2,5,3,4,6,2,2])
print_list( Solution().swapPairs(arr) )