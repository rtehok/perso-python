from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prev = prices[0]
        # profit = 0
        # for day in range(1, len(prices)):
        #     price = prices[day]
        #     if price >= prev:
        #         profit = max(profit, price - prev)
        #         prev = min(price, prev)
        #     else:
        #         prev = price
        # return profit

        # min = 0
        # max_profit = 0
        # for day, price in enumerate(prices):
        #     if prices[min] >= price:
        #         min = day
        #     max_profit = max(max_profit, price - prices[min])
        #
        # return max_profit

        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
