# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            dummy = ListNode(-1)
            tmp = dummy
            while left and right:
                if left.val < right.val:
                    tmp.next = left
                    tmp = tmp.next
                    left = left.next
                else:
                    tmp.next = right
                    tmp = tmp.next
                    right = right.next
            while left:
                tmp.next = left
                tmp = tmp.next
                left = left.next
            while right:
                tmp.next = right
                tmp = tmp.next
                right = right.next

            return dummy.next

        def mergeSort(start, end):
            if start == end:
                return lists[start]
            mid = (start + end) // 2
            left = mergeSort(start, mid)
            right = mergeSort(mid + 1, end)
            return merge(left, right)

        if not lists:
            return None

        return mergeSort(0, len(lists) - 1)


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    print(Solution().mergeKLists([l1, l2, l3]))
