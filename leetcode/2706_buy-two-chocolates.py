from typing import List


class Solution:
    def buyChocoSort(self, prices: List[int], money: int) -> int:
        prices.sort()
        remain = money - prices[0] - prices[1]
        return remain if remain >= 0 else money

    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum = min(prices[0], prices[1])
        second_min = max(prices[0], prices[1])

        for i in range(2, len(prices)):
            if prices[i] < minimum:
                second_min = minimum
                minimum = prices[i]
            elif prices[i] < second_min:
                second_min = prices[i]

        min_cost = minimum + second_min

        return money - min_cost if money - min_cost >= 0 else money


assert Solution().buyChoco([1, 2, 2], 3) == 0
assert Solution().buyChoco([3, 2, 3], 3) == 3
