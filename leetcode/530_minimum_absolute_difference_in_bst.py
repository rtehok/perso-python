# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def getMinimumDifferenceDFS(self, root: Optional[TreeNode]) -> int:
        a = []

        def dfs(node):
            if not node:
                return

            a.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        a.sort()
        min_diff = float("inf")
        for i in range(1, len(a)):
            min_diff = min(min_diff, a[i] - a[i - 1])

        return min_diff

    def getMinimumDifferenceInorderWithArray(self, root: Optional[TreeNode]) -> int:
        a = []

        def inOrder(node):
            if not node:
                return

            inOrder(node.left)
            a.append(node.val)
            inOrder(node.right)

        inOrder(root)

        min_diff = float("inf")
        for i in range(1, len(a)):
            min_diff = min(min_diff, a[i] - a[i - 1])

        return min_diff

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev = None

        def inOrder(node):
            if not node:
                return

            inOrder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inOrder(node.right)

        inOrder(root)

        return self.min_diff


if __name__ == "__main__":
    assert Solution().getMinimumDifference(build_tree([4, 2, 6, 1, 3])) == 1
    assert Solution().getMinimumDifference(build_tree([1, 0, 48, None, None, 12, 49])) == 1
    assert Solution().getMinimumDifference(build_tree([236, 104, 701, None, 227, None, 911])) == 9
    assert Solution().getMinimumDifference(build_tree([0, None, 2236, 1277, 2776, 519])) == 519
