from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        apply = {
            2: (lambda x, y: x or y),
            3: (lambda x, y: x and y)
        }

        def dfs(node):
            if node.left and node.right:
                left_val = dfs(node.left)
                right_val = dfs(node.right)
                return apply[node.val](left_val, right_val)

            return node.val

        return dfs(root)


assert Solution().evaluateTree(build_tree([2, 1, 3, None, None, 0, 1]))
assert not Solution().evaluateTree(build_tree([0]))
