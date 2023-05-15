from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = second = third = head

        while k >= 1:
            first = first.next
            if k > 1:
                third = third.next
            k -= 1

        while first:
            first = first.next
            second = second.next

        second.val, third.val = third.val, second.val

        return head


if __name__ == "__main__":
    assert compare_linked_lists(Solution().swapNodes(build_list([1, 2, 3, 4, 5]), k=2), build_list([1, 4, 3, 2, 5]))
    assert compare_linked_lists(Solution().swapNodes(build_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), k=5),
                                build_list([7, 9, 6, 6, 8, 7, 3, 0, 9, 5]))
