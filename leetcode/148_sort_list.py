from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # TC O(n * log(n)) / SC O(log(n))
    def sortListMS(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # divide
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode()
        tail = dummy

        # conquer
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next

            tail = tail.next

        tail.next = left or right

        return dummy.next

    # TC O(n * log(n)) / SC O(1)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count the length of the list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # init dummy and step
        dummy = ListNode()
        dummy.next = head
        step = 1

        while step < length:
            prev = dummy
            curr = dummy.next

            while curr:
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)
                prev = self.merge(left, right, prev)
            step *= 2

        return dummy.next

    def split(self, head, n):
        for i in range(n - 1):
            if not head:
                break
            head = head.next
        if not head:
            return None
        next_head = head.next
        head.next = None
        return next_head

    def merge(self, left, right, prev):
        tail = prev
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right

        while tail.next:
            tail = tail.next

        return tail


if __name__ == "__main__":
    Solution().sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
    Solution().sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))
