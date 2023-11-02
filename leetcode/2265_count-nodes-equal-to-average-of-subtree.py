import math
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def traverse(node, nb_child):
            nonlocal ans

            if not node:
                return 0, 0

            left_sum, left_nb = traverse(node.left, nb_child + 1)
            right_sum, right_nb = traverse(node.right, nb_child + 1)
            child_sum = node.val + left_sum + right_sum
            child_nb = 1 + left_nb + right_nb

            if child_sum // child_nb == node.val:
                ans += 1

            return child_sum, child_nb

        traverse(root, 1)
        return ans


if __name__ == "__main__":
    assert Solution().averageOfSubtree(build_tree([4, 8, 5, 0, 1, None, 6])) == 5
    assert Solution().averageOfSubtree(build_tree([1])) == 1
