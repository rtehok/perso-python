from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        mod = 10 ** 9 + 7
        m = len(group)

        dp = [[[-1] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m)]  # index, count, profit

        def traverse(index, count, cum_profit):
            if index == m:
                return 1 if cum_profit >= minProfit else 0

            if dp[index][count][cum_profit] != -1:
                return dp[index][count][cum_profit]

            res = traverse(index + 1, count, cum_profit)

            if count + group[index] <= n:
                res += traverse(index + 1, count + group[index],
                                min(minProfit, cum_profit + profits[index]))

            dp[index][count][cum_profit] = res % mod
            return dp[index][count][cum_profit]

        return traverse(0, 0, 0)

if __name__ == "__main__":
    assert Solution().profitableSchemes(n=5, minProfit=3, group=[2, 2], profits=[2, 3]) == 2
    assert Solution().profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profits=[6, 7, 8]) == 7
    assert Solution().profitableSchemes(n=1, minProfit=1, group=[2, 2, 2, 2, 2], profits=[1, 2, 1, 1, 0]) == 0
    assert Solution().profitableSchemes(n=64, minProfit=0, group=[80, 40], profits=[88, 88]) == 2
