import math
from typing import List


class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     dp = [[-1] * n for _ in range(n)]
    #     dp[n - 1] = triangle[n - 1]
    #
    #     for i in range(n - 2, -1, -1):
    #         for j in range(i + 1):
    #             lower_left = triangle[i][j] + dp[i + 1][j]
    #             lower_right = triangle[i][j] + dp[i + 1][j + 1]
    #             dp[i][j] = min(lower_left, lower_right)
    #
    #     return dp[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        next_row = triangle[-1][:]
        curr_row = [0] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + next_row[j]
                lower_right = triangle[i][j] + next_row[j + 1]
                curr_row[j] = min(lower_left, lower_right)

            curr_row, next_row = next_row, curr_row

        return next_row[0]


if __name__ == "__main__":
    assert Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]]) == -1
