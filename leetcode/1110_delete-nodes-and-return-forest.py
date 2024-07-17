from collections import deque
from typing import Optional, List

from leetcode.helpers.helpers import TreeNode


class Solution:
    def delNodesDFS(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None

            return node

        root = dfs(root)

        if root:
            res.append(root)

        return res

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        to_delete = set(to_delete)
        res = []

        q = deque([root])

        while q:
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
                if curr.left.val in to_delete:
                    curr.left = None

            if curr.right:
                q.append(curr.right)
                if curr.right.val in to_delete:
                    curr.right = None

            if curr.val in to_delete:
                if curr.left:
                    res.append(curr.left)
                if curr.right:
                    res.append(curr.right)

        if root.val not in to_delete:
            res.append(root)

        return res

