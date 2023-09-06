from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToPartsV1(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        width, remainder = divmod(n, k)

        res = []
        curr = head
        for i in range(k):
            root = write = ListNode()
            for j in range(width + (i < remainder)):
                write.next = ListNode(curr.val)
                write = write.next
                if curr:
                    curr = curr.next

            res.append(root.next)

        return res

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        width, remainder = divmod(n, k)

        res = []
        curr = head

        for i in range(k):
            root = curr
            for j in range(width + (i < remainder) - 1):
                if curr:
                    curr = curr.next
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp
            res.append(root)

        return res


if __name__ == "__main__":
    s = Solution().splitListToParts(head=ListNode(1, ListNode(2, ListNode(3))), k=5)
    assert s[0].val == 1
    assert s[1].val == 2
    assert s[2].val == 3
    assert s[3] is None
    assert s[4] is None

    s = Solution().splitListToParts(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                        ListNode(5, ListNode(6, ListNode(7, ListNode(8,
                                        ListNode(9, ListNode(10)))))))))), k=3)
    assert s[0].val == 1
    assert s[0].next.val == 2
    assert s[0].next.next.val == 3
    assert s[0].next.next.next.val == 4

    assert s[1].val == 5
    assert s[1].next.val == 6
    assert s[1].next.next.val == 7

    assert s[2].val == 8
    assert s[2].next.val == 9
    assert s[2].next.next.val == 10
