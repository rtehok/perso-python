from typing import List, Optional

from leetcode.helpers.helpers import TreeNode, is_same_tree, build_tree


class Solution:
    def generateTreesDFS(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def dfs(start, end):
            res = []
            if start > end:
                res.append(None)
                return res

            if (start, end) in memo:
                return memo[(start, end)]

            for i in range(start, end + 1):
                left_sub_tree = dfs(start, i - 1)
                right_sub_tree = dfs(i + 1, end)

                for left in left_sub_tree:
                    for right in right_sub_tree:
                        root = TreeNode(i, left, right)
                        res.append(root)

            memo[(start, end)] = res
            return res

        return dfs(1, n)

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = [TreeNode(i)]

        for numberOfNodes in range(2, n + 1):
            for start in range(1, n - numberOfNodes + 2):
                end = start + numberOfNodes - 1
                for i in range(start, end + 1):
                    left_subtrees = dp[start][i - 1] if i != start else [None]
                    right_subtrees = dp[i + 1][end] if i != end else [None]

                    for left in left_subtrees:
                        for right in right_subtrees:
                            root = TreeNode(i, left, right)
                            dp[start][end].append(root)

        return dp[1][n]


if __name__ == "__main__":
    res = Solution().generateTrees(3)
    assert is_same_tree(build_tree([1, None, 2, None, 3]), res[0])
    assert is_same_tree(build_tree([1, None, 3, 2]), res[1])
    assert is_same_tree(build_tree([2, 1, 3]), res[2])
    assert is_same_tree(build_tree([3, 1, None, None, 2]), res[3])
    assert is_same_tree(build_tree([3, 2, None, 1]), res[4])

    assert is_same_tree(build_tree([1]), Solution().generateTrees(1)[0])
