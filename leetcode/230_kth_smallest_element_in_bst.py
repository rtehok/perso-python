import collections
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    # O(n) / O(n)
    def kthSmallestDFS(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        def traverse(node):
            if not node:
                return []

            return traverse(node.left) + [node.val] + traverse(node.right)

        return traverse(root)[k - 1]

    # O(H + k) / O(H)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


if __name__ == "__main__":
    assert Solution().kthSmallest(root=build_tree([3, 1, 4, None, 2]), k=1) == 1
    assert Solution().kthSmallest(root=build_tree([5, 3, 6, 2, 4, None, None, 1]), k=3) == 3
