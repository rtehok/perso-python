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

        while first.next:
            first = first.next
            second = second.next

        if n > 0:
            return head.next

        second.next = second.next.next
        return head


if __name__ == "__main__":
    Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 1)
    Solution().removeNthFromEnd(ListNode(1), 1)
    Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)

