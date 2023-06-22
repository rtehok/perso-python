from typing import List


class Solution:
    def maxProfitRecursive(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        def calculateMaxProfit(i, has_stock, cash):
            if i >= n:
                return cash

            if has_stock:
                sell_profit = calculateMaxProfit(i + 1, False, cash + prices[i] - fee)
                hold_profit = calculateMaxProfit(i + 1, True, cash)
                return max(sell_profit, hold_profit)
            else:
                buy_profit = calculateMaxProfit(i + 1, True, cash - prices[i])
                skip_profit = calculateMaxProfit(i + 1, False, cash)
                return max(buy_profit, skip_profit)

        return calculateMaxProfit(0, False, 0)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]

    def maxProfitOptimized(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash


if __name__ == "__main__":
    assert Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2) == 8
    assert Solution().maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3) == 6
