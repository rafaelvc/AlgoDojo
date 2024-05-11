#https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, cur = head, head
        while cur.next:
            if cur.next.val != cur.val:
                prev.next = cur.next
                prev, cur = cur.next, cur.next
            else:
                cur = cur.next
        prev.next = None
        return head    