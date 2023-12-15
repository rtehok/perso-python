from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [0] * m
        ones_col = [0] * n
        zeros_row = [0] * m
        zeros_col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros_row[i] += 1
                    zeros_col[j] += 1
                else:
                    ones_row[i] += 1
                    ones_col[j] += 1

        diff = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        return diff


assert Solution().onesMinusZeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]]) == [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]
assert Solution().onesMinusZeros(grid=[[1, 1, 1], [1, 1, 1]]) == [[5, 5, 5], [5, 5, 5]]
