# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stack = [(root, float('-inf'), float('+inf'))]
        #
        # while stack:
        #     root, lower, upper = stack.pop()
        #
        #     if not root:
        #         continue
        #     if root.val <= lower or root.val >= upper:
        #         return False
        #     else:
        #         stack.append((root.left, lower, root.val))
        #         stack.append((root.right, root.val, upper))
        #
        # return True
        def helper(node, lower, upper):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root, float('-inf'), float('+inf'))


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().isValidBST(root)
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert not Solution().isValidBST(root)
