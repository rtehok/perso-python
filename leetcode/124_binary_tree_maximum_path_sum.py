import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -math.inf

        def dfs(node):
            nonlocal max_path_sum
            if not node:
                return 0

            left_sub_tree = max(dfs(node.left), 0)
            right_sub_tree = max(dfs(node.right), 0)

            max_path_sum = max(max_path_sum, left_sub_tree + right_sub_tree + node.val)

            return max(
                left_sub_tree + node.val,
                right_sub_tree + node.val,
            )

        dfs(root)
        return max_path_sum


if __name__ == "__main__":
    root = TreeNode(1,
                    TreeNode(2),
                    TreeNode(3)
                    )
    assert Solution().maxPathSum(root) == 6
    root = TreeNode(-10,
                    TreeNode(9),
                    TreeNode(20,
                             TreeNode(15),
                             TreeNode(7))
                    )
    assert Solution().maxPathSum(root) == 42
