from typing import List


class Solution:
    def changeTopDown(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n)]

        def dfs(idx, remaining):
            if remaining == 0:
                return 1

            if idx == n:
                return 0

            if memo[idx][remaining] != -1:
                return memo[idx][remaining]

            if coins[idx] > remaining:
                memo[idx][remaining] = dfs(idx + 1, remaining)  # skip
            else:
                memo[idx][remaining] = dfs(idx + 1, remaining) + dfs(idx, remaining - coins[idx])

            return memo[idx][remaining]

        return dfs(0, amount)

    def changeBottomUp(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]

        return dp[0][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)  # remove rows, as we only need previous row
        dp[0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(coins[i], amount + 1):  # change first coin as it is skipped if coins[i] > j
                dp[j] += dp[j - coins[i]]

        return dp[amount]


if __name__ == "__main__":
    assert Solution().change(amount=5, coins=[1, 2, 5]) == 4
    assert Solution().change(amount=3, coins=[2]) == 0
    assert Solution().change(amount=10, coins=[10]) == 1
