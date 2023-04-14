# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindromeV1(self, head: Optional[ListNode]) -> bool:
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        n = len(values)
        for i in range(n // 2):
            if values[i] != values[n - 1 - i]:
                return False

        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse in-place from middle
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == "__main__":
    assert not Solution().isPalindrome(ListNode(1, ListNode(1, ListNode(2, ListNode(1)))))
    assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
    assert not Solution().isPalindrome(ListNode(1, ListNode(2)))
