# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([])
        q.append(root.left)
        q.append(root.right)
        while q:
            left = q.popleft()
            right = q.popleft()

            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False

            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)

        return True

    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            return l.val == r.val and isMirror(l.right, r.left) and isMirror(l.left, r.right)

        return isMirror(root, root)


if __name__ == "__main__":
    assert Solution().isSymmetric(
        TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))
    assert not Solution().isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))))
