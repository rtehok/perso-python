from collections import deque
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def smallestFromLeafDFS(self, root: Optional[TreeNode]) -> str:
        self.smallest_string = ""

        def dfs(node, curr):
            if not node:
                return

            curr = chr(node.val + ord("a")) + curr

            if not node.left and not node.right:
                if not self.smallest_string or self.smallest_string > curr:
                    self.smallest_string = curr

            if node.left:
                dfs(node.left, curr)
            if node.right:
                dfs(node.right, curr)

        dfs(root, "")
        return self.smallest_string

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest_string = ""
        q = deque()
        q.append((root, chr(root.val + ord("a"))))

        while q:
            node, curr = q.popleft()

            if not node.left and not node.right:
                smallest_string = min(smallest_string, curr) if smallest_string else curr

            if node.left:
                q.append((node.left, chr(node.left.val + ord("a")) + curr))
            if node.right:
                q.append((node.right, chr(node.right.val + ord("a")) + curr))

        return smallest_string


assert Solution().smallestFromLeaf(build_tree([0, 1, 2, 3, 4, 3, 4])) == "dba"
assert Solution().smallestFromLeaf(build_tree([25, 1, 3, 1, 3, 0, 2])) == "adz"
assert Solution().smallestFromLeaf(build_tree([2, 2, 1, None, 1, 0, None, 0])) == "abc"
