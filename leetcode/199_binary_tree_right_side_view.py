import collections
from typing import Optional, List

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if node:
                if len(res) < level:
                    res.append(node.val)

                dfs(node.right, level + 1)
                dfs(node.left, level + 1)

        dfs(root, 1)

        return res

    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            while q_len:
                node = q.popleft()
                if q_len == 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                q_len -= 1

        return res


if __name__ == "__main__":
    assert Solution().rightSideView(build_tree([1, 2, 3, 4])) == [1, 3, 4]
    assert Solution().rightSideView(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert Solution().rightSideView(build_tree([1, None, 3])) == [1, 3]
    assert Solution().rightSideView(build_tree([1, 2])) == [1, 2]
