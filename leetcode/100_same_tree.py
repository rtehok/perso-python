# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q) or (p and q and p.val != q.val):
            return False

        if not p and not q:
            return True

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().isSameTree(p, q)
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert not Solution().isSameTree(p, q)
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert not Solution().isSameTree(p, q)
