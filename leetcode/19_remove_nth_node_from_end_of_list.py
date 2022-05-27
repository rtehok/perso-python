# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        while n > 0 and first.next:
            n -= 1
            first = first.next

        while first.next is not None:
            first = first.next
            second = second.next

        if n > 0:
            return head.next

        second.next = second.next.next
        return head
