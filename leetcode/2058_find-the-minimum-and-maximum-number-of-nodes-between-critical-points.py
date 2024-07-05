from typing import Optional, List

from leetcode.helpers.helpers import ListNode, build_list


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]

        b = c = 0
        first = prev = None
        i = 1
        min_dist = float("inf")

        while head:
            a, b, c = b, c, head.val
            if a and b and c and (a > b < c or a < b > c):
                if first is None:
                    first = i
                else:
                    min_dist = min(min_dist, i - prev)
                    res = [min_dist, i - first]

                prev = i

            i += 1
            head = head.next

        return res


assert Solution().nodesBetweenCriticalPoints(head=build_list([3, 1])) == [-1, -1]
assert Solution().nodesBetweenCriticalPoints(head=build_list([5, 3, 1, 2, 5, 1, 2])) == [1, 3]
assert Solution().nodesBetweenCriticalPoints(head=build_list([1, 3, 2, 2, 3, 2, 2, 2, 7])) == [3, 3]
