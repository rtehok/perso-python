from typing import List


class Solution:
    def maxProfitGreedy(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit

    def maxProfitRecursion(self, prices: List[int]) -> int:
        n = len(prices)

        # O(n2)
        def helper(i, buy):
            if i == n:
                return 0

            if buy:
                profit = max(
                    -prices[i] + helper(i + 1, 0),
                    0 + helper(i + 1, 1)
                )
            else:
                profit = max(
                    prices[i] + helper(i + 1, 1),
                    0 + helper(i + 1, 0)
                )

            return profit

        return helper(0, 1)

    def maxProfitTabulationAndArray(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [0, 0]
        current = [0, 0]

        for ind in range(n - 1, -1, -1):
            for buy in [0, 1]:
                if buy:
                    profit = max(
                        -prices[ind] + ahead[0],
                        0 + ahead[1]
                    )
                else:
                    profit = max(
                        prices[ind] + ahead[1],
                        0 + ahead[0]
                    )

                current[buy] = profit
            ahead = current

        return current[1]

    # space optimized
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ahead_buy, ahead_sell = 0, 0

        for ind in range(n - 1, -1, -1):
            current_buy = max(
                        -prices[ind] + ahead_sell,
                        0 + ahead_buy
                    )
            current_sell = max(
                        prices[ind] + ahead_buy,
                        0 + ahead_sell
                    )

            ahead_buy = current_buy
            ahead_sell = current_sell

        return ahead_buy


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
