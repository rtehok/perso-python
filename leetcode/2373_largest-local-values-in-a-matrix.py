from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                res[i - 1][j - 1] = max(
                    grid[i - 1][j],
                    grid[i - 1][j + 1],
                    grid[i][j - 1],
                    grid[i - 1][j - 1],
                    grid[i][j],
                    grid[i + 1][j],
                    grid[i + 1][j - 1],
                    grid[i][j + 1],
                    grid[i + 1][j + 1])

        return res


assert Solution().largestLocal(grid=[
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]]) == [[9, 9], [8, 6]]
assert Solution().largestLocal(
    grid=[[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]) == [[2, 2, 2],
                                [2, 2, 2],
                                [2, 2, 2]]
