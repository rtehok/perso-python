from typing import List


class Solution:
    def paintWallsTopDown(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        memo = [[0] * (n + 1) for _ in range(n)]

        def solve(i, remain):
            if remain <= 0:
                return 0
            if i == n:
                return float("inf")
            if memo[i][remain]:
                return memo[i][remain]

            paint = cost[i] + solve(i + 1, remain - 1 - time[i])
            dont_paint = solve(i + 1, remain)
            memo[i][remain] = min(paint, dont_paint)
            return memo[i][remain]

        return solve(0, n)

    def paintWallsBottomUp(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[n][i] = float("inf")

        for i in range(n - 1, -1, -1):
            for remain in range(1, n + 1):
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                dp[i][remain] = min(paint, dont_paint)

        return dp[0][n]

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp_prev = [float("inf")] * (n + 1)
        dp_prev[0] = 0

        for i in range(n - 1, -1, -1):
            dp = [0] * (n + 1)
            for remain in range(1, n + 1):
                paint = cost[i] + dp_prev[max(0, remain - 1 - time[i])]
                dont_paint = dp_prev[remain]
                dp[remain] = min(paint, dont_paint)

            dp_prev = dp

        return dp[n]


if __name__ == "__main__":
    assert Solution().paintWalls(cost=[1, 2, 3, 2], time=[1, 2, 3, 2]) == 3
    assert Solution().paintWalls(cost=[2, 3, 4, 2], time=[1, 1, 1, 1]) == 4
