import collections
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append(root)
        even = True

        while q:
            prev = float("inf")
            if even:
                prev = float("-inf")

            for _ in range(len(q)):
                curr = q.popleft()
                if (even and (curr.val % 2 == 0 or curr.val <= prev)) or \
                        (not even and (curr.val % 2 != 0 or curr.val >= prev)):
                    return False
                prev = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            even = not even

        return True


assert Solution().isEvenOddTree(build_tree([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]))
assert not Solution().isEvenOddTree(build_tree(
    [15, 26, 1, 1, 5, 43, 47, 26, 24, 20, None, 18, 16, 12, 8, None, None, None, None, None, None, None, None, None,
     None, 21]))
assert not Solution().isEvenOddTree(build_tree([2, 12, 8, 5, 9, None, None, 18, 16]))
assert not Solution().isEvenOddTree(build_tree([5, 9, 1, 3, 5, 7]))
assert not Solution().isEvenOddTree(build_tree([5, 4, 2, 3, 3, 7]))
