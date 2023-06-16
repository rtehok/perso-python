import collections
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def maxLevelSumBFS(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        level = 0
        ans = 0

        q = collections.deque([root])

        while q:
            q_len = len(q)
            q_sum = 0
            level += 1
            for _ in range(q_len):
                curr = q.popleft()

                q_sum += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if q_sum > max_sum:
                max_sum = q_sum
                ans = level

        return ans

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.sum_at_level = []

        def dfs(node, level):
            if node:
                if len(self.sum_at_level) == level:
                    self.sum_at_level.append(node.val)
                else:
                    self.sum_at_level[level] += node.val

                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)

        return self.sum_at_level.index(max(self.sum_at_level)) + 1


if __name__ == "__main__":
    assert Solution().maxLevelSum(build_tree([1, 1, 0, 7, -8, -7, 9])) == 1
    assert Solution().maxLevelSum(build_tree([-100, -200, -300, -20, -5, -10, None])) == 3
    assert Solution().maxLevelSum(build_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])) == 2
    assert Solution().maxLevelSum(build_tree([1, 7, 0, 7, -8, None, None])) == 2
