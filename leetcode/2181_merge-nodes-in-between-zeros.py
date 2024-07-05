from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    def mergeNodesV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        idx = set()
        i = 0
        while last.next:
            if last.val == 0:
                idx.add(i)
            last = last.next
            i += 1

        n = i

        dummy = ListNode(0)
        res = dummy
        curr = 0
        head = head.next
        i = 1
        while i < n:
            curr += head.val
            if 0 < i < n and i in idx:
                res.next = ListNode(curr)
                res = res.next
                curr = 0
            i += 1
            head = head.next

        res.next = ListNode(curr)
        return dummy.next

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        next_sum = modify

        while next_sum:
            sum = 0
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next

            modify.val = sum

            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next

        return head.next


assert compare_linked_lists(Solution().mergeNodes(build_list([0, 3, 1, 0, 4, 5, 2, 0])),
                            build_list([4, 11]))
assert compare_linked_lists(Solution().mergeNodes(build_list([0,1,0,3,0,2,2,0])),
                            build_list([1, 3, 4]))