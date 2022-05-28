# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        first = head
        third = first.next.next

        head = head.next
        head.next = first
        head.next.next = self.swapPairs(third)

        return head