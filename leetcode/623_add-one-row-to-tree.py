from collections import deque
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree, is_same_tree


class Solution:
    def addOneRowBFS(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        q = deque([(root, 1)])

        while q:
            curr, level = q.popleft()

            if level == depth - 1:
                left = curr.left
                right = curr.right

                curr.left = TreeNode(val, left=left)
                curr.right = TreeNode(val, right=right)
                continue

            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))

        return root

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, level):
            if not node:
                return

            if level > 2:
                dfs(node.left, level - 1)
                dfs(node.right, level - 1)
            else:
                left = node.left
                node.left = TreeNode(val, left=left)
                right = node.right
                node.right = TreeNode(val, right=right)

        if depth == 1:
            return TreeNode(val, left=root)

        dfs(root, depth)
        return root


assert is_same_tree(Solution().addOneRow(root=build_tree([4, 2, 6, 3, 1, 5]), val=1, depth=2),
                    build_tree([4, 1, 1, 2, None, None, 6, 3, 1, 5]))
assert is_same_tree(Solution().addOneRow(root=build_tree([4, 2, None, 3, 1]), val=1, depth=3),
                    build_tree([4, 2, None, 1, 1, 3, None, None, 1]))
