# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(head):
            prev = None
            while head:
                head.next, head, prev = prev, head.next, head
            return prev

        if not head or not head.next:
            return

        def merge(l1, l2):
            while l2:
                tmp = l1.next
                l1.next = l2
                l1 = l2
                l2 = tmp

        # h = l1: 1-2 / l2: 4-3
        # h: 1-4-3 / l1: 4-3 / l2: 2
        # h: 1-4-2 / l1: 2 / l2: 3
        # h: 1-4-2-3 / l1: 3 / l2: None

        slow = head
        fast = head
        prev = head

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        # h = 1-2-3-4 / prev = 2-3-4
        prev.next = None  # h = 1-2
        list1 = head
        list2 = reverse(slow)
        merge(list1, list2)


h = build_list([1, 2, 3, 4])
Solution().reorderList(h)
assert compare_linked_lists(h, build_list([1, 4, 2, 3]))

h = build_list([1, 2, 3, 4, 5])
Solution().reorderList(h)
assert compare_linked_lists(h, build_list([1, 5, 2, 4, 3]))
