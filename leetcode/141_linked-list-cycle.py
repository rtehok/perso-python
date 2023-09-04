# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional

from leetcode.helpers.helpers import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        if not head:
            return False

        while fast.next and fast.next.next:
            if fast.next == slow or fast.next.next == slow:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
