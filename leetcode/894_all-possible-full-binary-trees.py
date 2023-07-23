from typing import List, Optional

from leetcode.helpers.helpers import TreeNode, build_tree, is_same_tree


class Solution:
    def allPossibleFBTRecursive(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode()]

        res = []

        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)

        return res

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode())

        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                for left in dp[i]:
                    for right in dp[count - i - 1]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)

        return dp[n]


if __name__ == "__main__":
    res = Solution().allPossibleFBT(7)
    assert len(res) == 5
    assert is_same_tree(res[0], build_tree([0, 0, 0, None, None, 0, 0, None, None, 0, 0]))
    assert is_same_tree(res[1], build_tree([0, 0, 0, None, None, 0, 0, 0, 0]))
    assert is_same_tree(res[2], build_tree([0, 0, 0, 0, 0, 0, 0]))
    assert is_same_tree(res[3], build_tree([0, 0, 0, 0, 0, None, None, None, None, 0, 0]))
    assert is_same_tree(res[4], build_tree([0, 0, 0, 0, 0, None, None, 0, 0]))

    assert is_same_tree(Solution().allPossibleFBT(3)[0], build_tree([0, 0, 0]))
