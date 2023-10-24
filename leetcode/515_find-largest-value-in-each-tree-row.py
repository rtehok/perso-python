import collections
from typing import Optional, List

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root:
            q = collections.deque([root])
            while q:
                max_value = float("-inf")
                for _ in range(len(q)):
                    curr = q.popleft()
                    max_value = max(max_value, curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

                res.append(max_value)

        return res

    def largestValuesDFS(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, level):
            if not node:
                return

            if level == len(ans):
                ans.append(node.val)
            else:
                ans[level] = max(ans[level], node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return ans

    def largestValuesDFSIterative(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return []

        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()

            if level == len(ans):
                ans.append(node.val)
            else:
                ans[level] = max(ans[level], node.val)

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return ans


if __name__ == "__main__":
    assert Solution().largestValues(build_tree([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9]
    assert Solution().largestValues(build_tree([1, 2, 3])) == [1, 3]
