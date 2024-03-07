#https://leetcode.com/problems/add-two-numbers/

from typing import Optional
from merge_linked_lists import print_list, linked_list_from_arr, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        dez = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + dez
            dez = sum // 10
            n = ListNode( sum % 10 ) 
            if result is None:
                result = n
            else:
                prev.next = n
            prev = n            
            l1 = l1.next
            l2 = l2.next 
        if l2 is not None:
            l1 = l2
        while l1 is not None:
            sum = l1.val +  dez
            dez = sum // 10
            n = ListNode( sum % 10 ) 
            prev.next = n
            prev = n            
            l1 = l1.next 
        if dez > 0:
            n = ListNode( dez ) 
            prev.next = n
        return result

l1 = linked_list_from_arr([2,4,3])
l2 = linked_list_from_arr([5,6,4])
l3 = Solution().addTwoNumbers(l1, l2)
print_list(l3)

l1 = linked_list_from_arr([0])
l2 = linked_list_from_arr([0])
l3 = Solution().addTwoNumbers(l1, l2)
print_list(l3)

l1 = linked_list_from_arr([9,9,9,9,9,9,9])
l2 = linked_list_from_arr([9,9,9,9])
l3 = Solution().addTwoNumbers(l1, l2)
print_list(l3)