from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list


class Solution:
    def pairSumWithArray(self, head: Optional[ListNode]) -> int:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next

        i = 0
        j = len(values) - 1
        ans = 0
        while i < j:
            ans = max(ans, values[i] + values[j])
            i += 1
            j -= 1

        return ans

    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next  # reverse in-place

        start = head
        while prev:
            ans = max(ans, start.val + prev.val)
            prev = prev.next
            start = start.next

        return ans


if __name__ == "__main__":
    assert Solution().pairSum(build_list([5, 4, 2, 1])) == 6
    assert Solution().pairSum(build_list([4, 2, 2, 3])) == 7
    assert Solution().pairSum(build_list([1, 100000])) == 100001
