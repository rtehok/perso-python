import collections
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_width = 0

        q = collections.deque()
        q.append((root, 0))

        while q:
            q_len = len(q)
            _, index_start = q[0]
            index = 0
            for i in range(q_len):
                node, index = q.popleft()

                # from node at index i, construct next left index = 2 * i
                # from node at index i, construct next right index = 2 * i + 1
                if node.left:
                    q.append((node.left, 2 * index))
                if node.right:
                    q.append((node.right, 2 * index + 1))

            # index is always the last node from the queue

            self.max_width = max(self.max_width, index - index_start + 1)  # width = len + 1

        return self.max_width


if __name__ == "__main__":
    assert Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5, 3, None, 9])) == 4
    assert Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
    assert Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5])) == 2
    assert Solution().widthOfBinaryTree(build_tree([1, 3, 2, 5, 3, None, 9])) == 2
