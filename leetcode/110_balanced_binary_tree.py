from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0

            left_h, right_h = helper(node.left), helper(node.right)
            if left_h < 0 or right_h < 0 or abs(left_h - right_h) > 1:
                return -1

            return max(left_h, right_h) + 1

        return helper(root) >= 0


if __name__ == "__main__":
    assert Solution().isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    assert not Solution().isBalanced(
        TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)))
