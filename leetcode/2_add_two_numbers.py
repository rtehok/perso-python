# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def loop(first, second, carry) -> Optional[ListNode]:
            if first is None and second is None:
                return ListNode(carry) if carry > 0 else None
            elif first is None:
                sum = second.val + carry
                return ListNode(sum % 10, loop(None, second.next, sum // 10))
            elif second is None:
                sum = first.val + carry
                return ListNode(sum % 10, loop(first.next, None, sum // 10))
            else:
                sum = first.val + second.val + carry
                return ListNode(sum % 10, loop(first.next, second.next, sum // 10))

        return loop(l1, l2, 0)
