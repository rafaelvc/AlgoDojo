# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # We can check the cycle using obj id instead of val
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        nodes_ids = set( [id(head)] )
        node = head
        while node.next != None:
            if id(node.next) in nodes_ids:
                return True
            nodes_ids.add ( id(node) ) 
            node = node.next
        return False