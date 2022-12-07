# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return self.res

        self.res += root.val if root.val <= high and root.val >= low else 0
        if root.val >= low:
            self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            self.rangeSumBST(root.right, low, high)

        return self.res


if __name__ == "__main__":
    bst = TreeNode(10, left=TreeNode(5, TreeNode(3), TreeNode(7)), right=TreeNode(15, None, TreeNode(18)))
    assert Solution().rangeSumBST(bst, 7, 15) == 32

    bst = TreeNode(10, left=TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
                   right=TreeNode(15, TreeNode(13), TreeNode(18)))
    assert Solution().rangeSumBST(bst, 6, 10) == 23
