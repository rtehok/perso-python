import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TC: O(N)
# SC: O(N)
class SolutionLinear:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.arr[int(random.random() * len(self.arr))]


# TC: O(N)
# SC: O(1)
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            if random.random() < 1 / scope:
                chosen_value = curr.val

            curr = curr.next
            scope += 1

        return chosen_value


if __name__ == "__main__":
    l = Solution(ListNode(10, ListNode(1, ListNode(10, ListNode(20, ListNode(100))))))
    print(l.getRandom())
    print(l.getRandom())
    print(l.getRandom())
    print(l.getRandom())
