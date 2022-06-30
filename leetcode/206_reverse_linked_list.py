# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return tmp

        # prev = None
        # while head:
        #     tmp = head.next
        #     head.next = prev
        #     prev = head
        #     head = tmp
        # return prev


if __name__ == "__main__":
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().reverseList(root))
    root = ListNode(1, ListNode(2))
    print(Solution().reverseList(root))
