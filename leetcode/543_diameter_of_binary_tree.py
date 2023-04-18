from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def helper(node):
            if not node:
                return 0

            left_h = helper(node.left)
            right_h = helper(node.right)
            self.max_diameter = max(self.max_diameter, left_h + right_h)

            return max(left_h, right_h) + 1

        helper(root)
        return self.max_diameter


if __name__ == "__main__":
    assert Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3
    assert Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1
