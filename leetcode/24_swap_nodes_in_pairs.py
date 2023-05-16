# Definition for singly-linked list.
from typing import Optional

from leetcode.helpers.helpers import build_list, compare_linked_lists


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


if __name__ == "__main__":
    assert compare_linked_lists(Solution().swapPairs(build_list([1, 2, 3, 4])),
                                build_list([2, 1, 4, 3]))
    assert compare_linked_lists(Solution().swapPairs(build_list([])),
                                build_list([]))
