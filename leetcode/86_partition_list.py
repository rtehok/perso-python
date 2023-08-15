from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x_head = less_than_x_tail = ListNode(0)
        greater_than_x_head = greater_than_x_tail = ListNode(0)

        current = head

        while current:
            if current.val < x:
                less_than_x_tail.next = current
                less_than_x_tail = less_than_x_tail.next
            else:
                greater_than_x_tail.next = current
                greater_than_x_tail = greater_than_x_tail.next

            current = current.next

        less_than_x_tail.next = greater_than_x_head.next
        greater_than_x_tail.next = None

        return less_than_x_head.next


if __name__ == "__main__":
    assert compare_linked_lists(Solution().partition(build_list([1, 4, 3, 2, 5, 2]), 3), build_list([1, 2, 2, 4, 3, 5]))
    assert compare_linked_lists(Solution().partition(build_list([2, 1]), 2), build_list([1, 2]))
