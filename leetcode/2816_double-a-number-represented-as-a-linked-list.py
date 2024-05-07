from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    def doubleItReverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node
            return prev

        reversed = reverse(head)
        carry = 0
        curr, prev = reversed, None

        while curr:
            new_val = curr.val * 2 + carry
            curr.val = new_val % 10
            carry = 1 if new_val > 9 else 0
            prev, curr = curr, curr.next

        if carry:
            prev.next = ListNode(carry)

        return reverse(reversed)

    def doubleItStack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        val = 0
        while head:
            values.append(head.val)
            head = head.next

        new_tail = None

        while values or val != 0:
            new_tail = ListNode(0, new_tail)
            if values:
                val += values.pop() * 2
            new_tail.val = val % 10
            val //= 10

        return new_tail

    def doubleItRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def twice_of_val(head):
            if not head:
                return 0

            doubled_value = head.val * 2 + twice_of_val(head.next)
            head.val = doubled_value % 10

            return doubled_value // 10

        carry = twice_of_val(head)
        if carry:
            head = ListNode(carry, head)

        return head

    def doubleItTwoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            twice_of_val = curr.val * 2

            if twice_of_val < 10:
                curr.val = twice_of_val
            elif prev:
                curr.val = twice_of_val % 10
                prev.val += 1
            else:
                head = ListNode(1, head)
                curr.val = twice_of_val % 10

            prev, curr = curr, curr.next

        return head

    # Single pointer
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)

        node = head
        while node:
            node.val = (node.val * 2) % 10
            if node.next and node.next.val > 4:
                node.val += 1

            node = node.next

        return head


assert compare_linked_lists(Solution().doubleIt(build_list([1, 8, 9])), build_list([3, 7, 8]))
assert compare_linked_lists(Solution().doubleIt(build_list([9, 9, 9])), build_list([1, 9, 9, 8]))
