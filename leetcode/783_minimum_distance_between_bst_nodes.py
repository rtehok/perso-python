# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBSTWithArray(self, root: Optional[TreeNode]) -> int:
        in_order_nodes = []

        def dfs(node):
            nonlocal in_order_nodes
            if not node:
                return

            dfs(node.left)
            in_order_nodes.append(node.val)
            dfs(node.right)

        dfs(root)

        min_diff = math.inf

        for i in range(len(in_order_nodes) - 1):
            min_diff = min(min_diff, abs(in_order_nodes[i] - in_order_nodes[i + 1]))

        return min_diff

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = math.inf
        previous_node = None

        def dfs(node):
            nonlocal min_diff, previous_node
            if not node:
                return

            dfs(node.left)
            if previous_node:
                min_diff = min(min_diff, node.val - previous_node.val)

            previous_node = node

            dfs(node.right)

        dfs(root)

        return min_diff


if __name__ == "__main__":
    assert Solution().minDiffInBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))) == 1
    assert Solution().minDiffInBST(TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))) == 1
    assert Solution().minDiffInBST(
        TreeNode(90, TreeNode(69, TreeNode(49, None, TreeNode(52)), TreeNode(89)), None)) == 1
