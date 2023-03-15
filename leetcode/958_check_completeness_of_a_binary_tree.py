import collections
from typing import Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTreeV1(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([])
        q.append(root)

        while q:
            q_len = len(q)
            toggle = False
            has_next = False

            while q_len:
                node = q.popleft()

                if not node:
                    toggle = True

                if (node and toggle) or (not node and has_next):
                    return False

                if node:
                    if node.left or node.right:
                        has_next = True
                    q.append(node.left)
                    q.append(node.right)

                q_len -= 1

        return True

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([])
        q.append(root)

        none_found = False

        while q:
            node = q.popleft()

            if node is None:
                none_found = True
            else:
                if none_found:
                    return False

                q.append(node.left)
                q.append(node.right)

        return True


if __name__ == "__main__":
    assert Solution().isCompleteTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))))
    assert not Solution().isCompleteTree(
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7))))
    assert not Solution().isCompleteTree(TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, TreeNode(7), TreeNode(8))))
