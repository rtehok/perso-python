from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        i = 0
        res = 0
        while i <= len(costs) - 1:
            if costs[i] <= coins:
                res += 1
                coins -= costs[i]
            else:
                return res

            i += 1

        return res


if __name__ == "__main__":
    assert Solution().maxIceCream(costs=[1, 3, 2, 4, 1], coins=7) == 4
    assert Solution().maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5) == 0
    assert Solution().maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20) == 6
