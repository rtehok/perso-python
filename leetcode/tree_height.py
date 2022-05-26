from collections import deque
from typing import List


# A Tree node
class Node:
    def __init__(self):
        self.key = 0
        self.left, self.right = None, None


# Utility function to create a new node
def newNode(key):
    temp = Node()
    temp.key = key
    temp.left, temp.right = None, None
    return temp


class Solution:
    def height(self, root):
        if not root:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def olt_height(self, root):
        q = deque()
        q.append(root)
        q.append(None)

        res = 0

        while q:
            p = q.popleft()

            if p is None:
                res += 1

            if p is not None:
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)

            elif len(q):
                q.append(None)

        return res

    def iterative_height(self, root):
        h = 0
        q = deque()
        q.append(root)

        while True:
            node_count = len(q)

            if node_count == 0:
                return h

            h += 1

            while node_count > 0:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                node_count -= 1


if __name__ == "__main__":
    # Let us create Binary Tree shown in above example
    root = newNode(1)
    root.left = newNode(12)
    root.right = newNode(13)

    root.right.left = newNode(14)
    root.right.right = newNode(15)

    root.right.left.left = newNode(21)
    root.right.left.right = newNode(22)
    root.right.right.left = newNode(23)
    root.right.right.right = newNode(24)

    print(Solution().height(root))
    print(Solution().olt_height(root))
    print(Solution().iterative_height(root))
