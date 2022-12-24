from typing import List


class Solution:
    def maxProfitRecursive(self, prices: List[int]) -> int:
        n = len(prices)

        def helper(i, buy):
            if i >= n:
                return 0
            if buy:
                # buy at day i
                profit = max(-prices[i] + helper(i + 1, buy=0), 0 + helper(i + 1, buy=1))
            else:
                profit = max(prices[i] + helper(i + 2, buy=1), 0 + helper(i + 1, buy=0))
            return profit

        res = helper(0, 1)
        return res

    def maxProfitTabulation(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for buy in [0, 1]:
                if buy:
                    dp[i][buy] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
                else:
                    dp[i][buy] = max(prices[i] + dp[i + 2][1], 0 + dp[i + 1][0])

        return dp[0][1]

    def maxProfitTabulation(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            dp[i][0] = max(prices[i] + dp[i + 2][1], 0 + dp[i + 1][0])

        return dp[0][1]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        front2 = [0, 0]
        front1 = [0, 0]
        current = [0, 0]

        for i in range(n - 1, -1, -1):
            current[1] = max(-prices[i] + front1[0], 0 + front1[1])
            current[0] = max(prices[i] + front2[1], 0 + front1[0])

            front2 = front1.copy()
            front1 = current.copy()

        return current[1]


if __name__ == "__main__":
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3
    assert Solution().maxProfit([1]) == 0
    assert Solution().maxProfit(
        [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15,
         11, 94]) == 428
