import collections
from typing import Optional, List

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def findModeDFS(self, root: Optional[TreeNode]) -> List[int]:
        cnt = collections.defaultdict(int)

        def traverse(node):
            if not node:
                return

            cnt[node.val] += 1
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        max_nb_nodes = max(cnt.values())

        return [x for x, c in cnt.items() if c == max_nb_nodes]

    def findModeDFSStack(self, root: Optional[TreeNode]) -> List[int]:
        cnt = collections.defaultdict(int)

        stack = [root]

        while stack:
            node = stack.pop()
            cnt[node.val] += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        max_nb_nodes = max(cnt.values())

        return [x for x, c in cnt.items() if c == max_nb_nodes]

    def findModeBFS(self, root: Optional[TreeNode]) -> List[int]:
        cnt = collections.defaultdict(int)
        q = collections.deque([root])

        while q:
            node = q.popleft()
            cnt[node.val] += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        max_nb_nodes = max(cnt.values())

        return [x for x, c in cnt.items() if c == max_nb_nodes]

    def findModeWithValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, values):
            if not node:
                return

            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)

        values = []
        dfs(root, values)

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        for num in values:
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                max_streak = curr_streak
                ans = []

            if curr_streak == max_streak:
                ans.append(num)

        return ans

    def findModeInorder(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                return

            dfs(node.left)

            if node.val == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = node.val

            if curr_streak > max_streak:
                max_streak = curr_streak
                ans = []

            if curr_streak == max_streak:
                ans.append(node.val)

            dfs(node.right)

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        dfs(root)
        return ans

    # Morris Traversal
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        curr = root

        while curr:
            if curr.left:
                # find friend
                friend = curr.left
                while friend.right:
                    friend = friend.right

                friend.right = curr

                # delete edge
                left = curr.left
                curr.left = None
                curr = left

            else:
                # handle current node
                num = curr.val

                if num == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num

                if curr_streak > max_streak:
                    max_streak = curr_streak
                    ans = []

                if curr_streak == max_streak:
                    ans.append(num)

                curr = curr.right

        return ans


if __name__ == "__main__":
    assert Solution().findMode(build_tree([1, None, 2, 2])) == [2]
    assert Solution().findMode(build_tree([0])) == [0]
