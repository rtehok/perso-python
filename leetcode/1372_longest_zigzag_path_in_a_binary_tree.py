from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def traverse(node, go_left, steps):
            if node:
                self.count = max(self.count, steps)

                if go_left:
                    traverse(node.left, False, steps + 1)
                    traverse(node.right, True, 1)
                else:
                    traverse(node.left, False, 1)
                    traverse(node.right, True, steps + 1)

        traverse(root, True, 0)

        return self.count


if __name__ == "__main__":
    lst = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]
    assert Solution().longestZigZag(build_tree(lst)) == 3
    lst = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    assert Solution().longestZigZag(build_tree(lst)) == 4
