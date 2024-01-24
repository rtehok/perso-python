from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                path = path ^ (1 << node.val)
                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)

        count = 0
        preorder(root, 0)
        return count


assert Solution().pseudoPalindromicPaths(build_tree([2, 3, 1, 3, 1, None, 1])) == 2
assert Solution().pseudoPalindromicPaths(build_tree([2, 1, 1, 1, 3, None, None, None, None, None, 1])) == 1
assert Solution().pseudoPalindromicPaths(build_tree([9])) == 1
