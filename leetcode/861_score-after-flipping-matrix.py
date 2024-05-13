from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        for j in range(1, n):
            count_zero = 0
            for i in range(m):
                if grid[i][j] == 0:
                    count_zero += 1
            if count_zero > m - count_zero:  # more 0 than 1
                for i in range(m):
                    grid[i][j] ^= 1

        score = 0

        for i in range(m):
            for j in range(n):
                col_score = grid[i][j] << (n - j - 1)
                score += col_score
        return score


assert Solution().matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39
assert Solution().matrixScore(grid=[[0]]) == 1
