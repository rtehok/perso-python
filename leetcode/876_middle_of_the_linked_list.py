# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        i = 0
        while first.next:
            i += 1
            first = first.next

        i = i // 2 if i % 2 == 0 else i // 2 + 1

        while i > 0:
            head = head.next
            i -= 1

        return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert Solution().middleNode(head) == ListNode(3, ListNode(4, ListNode(5)))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,  ListNode(6))))))
    assert Solution().middleNode(head) == ListNode(4, ListNode(5,  ListNode(6)))

