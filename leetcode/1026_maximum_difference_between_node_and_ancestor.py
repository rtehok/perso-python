# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # brute force O(n2)
    def maxAncestorDiffBruteForce(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ancestors, max_diff) -> int:
            if node:
                max_diff = max(max_diff,
                               max([abs(ancestor - node.val) for ancestor in ancestors])) if ancestors else max_diff

                max_diff = dfs(node.left, ancestors + [node.val], max_diff)
                max_diff = dfs(node.right, ancestors + [node.val], max_diff)

            return max_diff

        return dfs(root, [], 0)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, curr_max, curr_min) -> int:
            if not node:
                return curr_max - curr_min

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            left = dfs(node.left, curr_max, curr_min)
            right = dfs(node.right, curr_max, curr_min)

            return max(left, right)

        return dfs(root, root.val, root.val)


if __name__ == "__main__":
    root = TreeNode(8,
                    TreeNode(3,
                             TreeNode(1),
                             TreeNode(6,
                                      TreeNode(4),
                                      TreeNode(7)
                                      )
                             ),
                    TreeNode(10,
                             None,
                             TreeNode(14,
                                      TreeNode(13),
                                      )
                             )
                    )
    assert Solution().maxAncestorDiff(root) == 7
    root = TreeNode(1,
                    None,
                    TreeNode(2,
                             None,
                             TreeNode(0,
                                      TreeNode(3))))
    assert Solution().maxAncestorDiff(root) == 3
