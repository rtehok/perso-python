from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, n, m):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] != 1:
                return 0

            grid[i][j] = '$'

            if 0 <= i <= m - 1 and 0 <= j <= n - 1:
                return 1 + dfs(i + 1, j, n, m) + dfs(i - 1, j, n, m) + dfs(i, j + 1, n, m) + dfs(i, j - 1, n, m)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = dfs(i, j, n, m)
                    res = max(curr, res)
        return res


if __name__ == "__main__":
    assert Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
