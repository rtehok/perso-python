from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycleHashSet(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_map = set()

        while head:
            if head in node_map:
                return head

            node_map.add(head)
            head = head.next

        return head

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None


if __name__ == "__main__":
    head = ListNode(1)
    t = ListNode(2)
    head.next = t
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    assert Solution().detectCycle(head) == t

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert Solution().detectCycle(head) is None


