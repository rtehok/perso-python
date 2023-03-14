# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, res):
            if not node.left and not node.right:
                return res + node.val

            left, right = 0, 0

            if node.left:
                left = helper(node.left, (res + node.val) * 10)
            if node.right:
                right = helper(node.right, (res + node.val) * 10)

            return left + right

        return helper(root, 0)


if __name__ == "__main__":
    assert Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
    assert Solution().sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))) == 1026
    assert Solution().sumNumbers(TreeNode(0, TreeNode(1))) == 1
