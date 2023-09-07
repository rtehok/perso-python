from typing import Optional

from leetcode.helpers.helpers import build_list, compare_linked_lists, ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next  # move to node next to left

        curr = prev.next

        for _ in range(right - left):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

        return dummy.next


if __name__ == "__main__":
    assert compare_linked_lists(Solution().reverseBetween(build_list([3, 5]), 1, 2),
                                build_list([5, 3]))
    assert compare_linked_lists(Solution().reverseBetween(build_list([1, 2, 3, 4, 5]), 2, 4),
                                build_list([1, 4, 3, 2, 5]))
    assert compare_linked_lists(Solution().reverseBetween(build_list([5]), 1, 1),
                                build_list([5]))
