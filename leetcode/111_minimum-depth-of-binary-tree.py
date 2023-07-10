import collections
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def minDepthDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, cnt, height):
            if node and not node.left and not node.right:
                return cnt, height

            min_cnt_left = min_height_left = min_cnt_right = min_height_right = float("inf")

            if node.left:
                min_cnt_left, min_height_left = dfs(node.left, cnt + 1, height + 1)
            if node.right:
                min_cnt_right, min_height_right = dfs(node.right, cnt + 1, height + 1)

            if min_height_left > min_height_right:
                return min_cnt_right, min_height_right
            else:
                return min_cnt_left, min_height_left

        return dfs(root, 1, 0)[0]

    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            if not node.left:
                return 1 + dfs(node.right)
            if not node.right:
                return 1 + dfs(node.left)

            return 1 + min(dfs(node.left), dfs(node.right))

        return dfs(root)


    def minDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque([(root, 1)])
        while q:
            curr, cnt = q.popleft()

            if curr.left:
                q.append((curr.left, cnt + 1))
            if curr.right:
                q.append((curr.right, cnt + 1))
            if not curr.left and not curr.right:
                return cnt
        return 0


if __name__ == "__main__":
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().minDepth(root) == 2
    root = build_tree([1, 2, 3, 4, 5])
    assert Solution().minDepth(root) == 2
    root = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    assert Solution().minDepth(root) == 5
