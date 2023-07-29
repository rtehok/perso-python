import collections
import math


class Solution:
    def soupServingsBottomUp(self, n: int) -> float:
        m = math.ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] + dp[max(0, i - 2)][max(0, j - 2)] + dp[i - 1][
                max(0, j - 3)]) / 4

        dp[0] = {0: 0.5}
        for k in range(1, m + 1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k + 1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)

            if dp[k][k] > 1 - 10 ** -5:
                return 1

        return dp[m][m]

    def soupServings(self, n: int) -> float:
        m = math.ceil(n / 25)
        dp = collections.defaultdict(dict)

        def calculate_dp(i, j):
            if i <= 0 and j <= 0:
                return 0.5

            if i <= 0:
                return 1

            if j <= 0:
                return 0

            if i in dp and j in dp[i]:
                return dp[i][j]

            dp[i][j] = (
                               calculate_dp(i - 4, j) +
                               calculate_dp(i - 3, j - 1) +
                               calculate_dp(i - 2, j - 2) +
                               calculate_dp(i - 1, j - 3)
                       ) / 4

            return dp[i][j]

        for k in range(1, m + 1):
            if calculate_dp(k, k) > 1 - 10 ** -5:
                return 1.0

        return calculate_dp(m, m)


if __name__ == "__main__":
    assert Solution().soupServings(50) == 0.62500
    assert Solution().soupServings(100) == 0.71875
