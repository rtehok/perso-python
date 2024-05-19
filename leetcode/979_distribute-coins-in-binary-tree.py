from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            left_coins = dfs(node.left)
            right_coins = dfs(node.right)

            self.moves += abs(left_coins) + abs(right_coins)

            return (node.val - 1) + left_coins + right_coins

        dfs(root)

        return self.moves


assert Solution().distributeCoins(build_tree([3, 0, 0])) == 2
assert Solution().distributeCoins(build_tree([0, 3, 0])) == 3
