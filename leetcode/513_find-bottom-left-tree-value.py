import collections
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def findBottomLeftValueDFS(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        left_most = 0

        def dfs(node, depth):
            nonlocal max_depth, left_most
            if not node:
                return

            if depth > max_depth:
                max_depth = depth
                left_most = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return left_most

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        curr = root
        q.append(root)

        while q:
            curr = q.popleft()
            if curr.right:
                q.append(curr.right)

            if curr.left:
                q.append(curr.left)

        return curr.val


assert Solution().findBottomLeftValue(build_tree([2, 1, 3])) == 1
assert Solution().findBottomLeftValue(build_tree([1, 2, 3, 4, None, 5, 6, None, None, 7])) == 7
