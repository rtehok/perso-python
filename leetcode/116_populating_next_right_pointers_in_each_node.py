from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = deque()
        q.append([root, 0])
        while q:
            node, level = q.popleft()

            if q and level == q[0][1]:
                node.next = q[0][0]

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return root


if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    Solution().connect(root)
    print(root)
