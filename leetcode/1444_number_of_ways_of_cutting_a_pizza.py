from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])

        apples = [[0] * (cols + 1) for row in range(rows + 1)]  # cumulative region sum matrix
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                apples[row][col] = (pizza[row][col] == "A") + apples[row + 1][col] + apples[row][col + 1] - \
                                   apples[row + 1][col + 1]

        dp = [[[0] * cols for row in range(rows)] for remain in range(k)]

        dp[0] = [[int(apples[row][col] > 0) for col in range(cols)] for row in range(rows)]

        mod = 10 ** 9 + 7

        for remain in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    for next_row in range(row + 1, rows):
                        if apples[row][col] - apples[next_row][col] > 0:
                            val += dp[remain - 1][next_row][col]
                    for next_col in range(col + 1, cols):
                        if apples[row][col] - apples[row][next_col] > 0:
                            val += dp[remain - 1][row][next_col]
                    dp[remain][row][col] = val % mod

        return dp[k - 1][0][0]


if __name__ == "__main__":
    assert Solution().ways(pizza=["A..",
                                  "AAA",
                                  "..."], k=3) == 3
    assert Solution().ways(pizza=["A..", "AA.", "..."], k=3) == 1
    assert Solution().ways(pizza=["A..", "A..", "..."], k=1) == 1
