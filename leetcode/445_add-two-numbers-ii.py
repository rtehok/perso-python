from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    # TC O(m + n) / SC O(m + 1)
    def addTwoNumbersWithStack(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2

        a1 = []
        a2 = []

        while first:
            a1.append(first.val)
            first = first.next

        while second:
            a2.append(second.val)
            second = second.next

        total_sum = 0
        carry = 0
        ans = ListNode()
        while a1 or a2:
            if a1:
                total_sum += a1.pop()
            if a2:
                total_sum += a2.pop()

            ans.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry

        return ans.next if carry == 0 else ans

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp

            return prev

        r1 = reverse(l1)
        r2 = reverse(l2)

        total_sum = 0
        carry = 0
        ans = ListNode()
        while r1 or r2:
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next
            ans.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry

        return ans.next if carry == 0 else ans


if __name__ == "__main__":
    assert compare_linked_lists(Solution().addTwoNumbers(l1=build_list([7, 2, 4, 3]), l2=build_list([5, 6, 4])),
                                build_list([7, 8, 0, 7]))
    assert compare_linked_lists(Solution().addTwoNumbers(l1=build_list([2, 4, 3]), l2=build_list([5, 6, 4])),
                                build_list([8, 0, 7]))
    assert compare_linked_lists(Solution().addTwoNumbers(l1=build_list([0]), l2=build_list([0])),
                                build_list([0]))
