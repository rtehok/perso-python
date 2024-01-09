# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilarV1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        def traverse(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)

            if root.left:
                traverse(root.left, leaves)
            if root.right:
                traverse(root.right, leaves)

        traverse(root1, leaves1)
        traverse(root2, leaves2)
        return leaves1 == leaves2

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        return list(dfs(root1)) == list(dfs(root2))


if __name__ == "__main__":
    root1 = TreeNode(3,
                     TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                     TreeNode(1, TreeNode(9), TreeNode(8)),
                     )
    root2 = TreeNode(3,
                     TreeNode(5, TreeNode(6), TreeNode(7)),
                     TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))),
                     )
    assert Solution().leafSimilar(root1, root2)
    assert not Solution().leafSimilar(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2)))
    assert not Solution().leafSimilar(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2)))
    assert Solution().leafSimilar(TreeNode(1, TreeNode(2)), TreeNode(2, TreeNode(2)))
