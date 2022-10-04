# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def loop(node, sum, res):
            if not node.left and not node.right:
                return sum + node.val == targetSum

            if node.left:
                res |= loop(node.left, sum + node.val, res)

            if node.right:
                res |= loop(node.right, sum + node.val, res)

            return res

        return loop(root, 0, False)
