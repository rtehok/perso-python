from math import inf
from typing import List


class Solution:
    def minFallingPathSumTLE(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}

        def dfs(r, c):
            if r == n - 1:
                return grid[r][c]

            if (r, c) in memo:
                return memo[(r, c)]

            next_min = inf
            for next_row_col in range(n):
                if next_row_col != c:
                    next_min = min(next_min, dfs(r + 1, next_row_col))
            memo[(r, c)] = grid[r][c] + next_min
            return memo[(r, c)]

        ans = inf
        for col in range(n):
            ans = min(ans, dfs(0, col))

        return ans

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = [[inf] * n for _ in range(n)]

        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]

        for row in range(n - 2, -1, - 1):
            for col in range(n):
                next_min = inf
                for next_row_col in range(n):
                    if next_row_col != col:
                        next_min = min(next_min, memo[row + 1][next_row_col])
                memo[row][col] = grid[row][col] + next_min

        ans = inf
        for col in range(n):
            ans = min(ans, memo[0][col])

        return ans


assert Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
