# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        def dfs(root, level):
            if not root:
                return 0

            if not root.left and not root.right:
                return level

            return max(dfs(root.left, level + 1), dfs(root.right, level + 1))

        return dfs(root, 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = collections.deque([(root, 1)])

        res = 1
        while q:
            next_node, level = q.popleft()
            res = level
            if next_node.left:
                q.append((next_node.left, level + 1))

            if next_node.right:
                q.append((next_node.right, level + 1))

        return res


if __name__ == "__main__":
    assert Solution().maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 3
    assert Solution().maxDepth(TreeNode(1, None, TreeNode(2))) == 2
    assert Solution().maxDepth(None) == 0
