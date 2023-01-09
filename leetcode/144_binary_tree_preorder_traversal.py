import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalDFS(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        def dfs(root):
            if not root:
                return

            res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res


if __name__ == "__main__":
    assert Solution().preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 2, 3]
    assert Solution().preorderTraversal(None) == []
    assert Solution().preorderTraversal(TreeNode(1)) == [1]
    assert Solution().preorderTraversal(TreeNode(1, TreeNode(4, TreeNode(2)), TreeNode(3))) == [1, 4, 2, 3]
