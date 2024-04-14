from collections import deque
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def sumOfLeftLeavesDFS(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0

            if not node.left and not node.right and is_left:
                return node.val

            left_sum = dfs(node.left, True)
            right_sum = dfs(node.right, False)

            return left_sum + right_sum

        return dfs(root, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, False)])

        total_sum = 0

        while q:
            node, is_left = q.popleft()
            if is_left and not node.left and not node.right:
                total_sum += node.val

            if node.left:
                q.append((node.left, True))
            if node.right:
                q.append((node.right, False))

        return total_sum


assert Solution().sumOfLeftLeaves(build_tree([3, 9, 20, None, None, 15, 7])) == 24
