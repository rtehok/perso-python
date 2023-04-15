import heapq
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # Let dp[i][coins] be the maximum total value of coins you can have in your wallet
        # if you choose at most "coins" coins from the leftmost "i" piles optimally.
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for coins in range(k + 1):
                current_sum = 0
                for current_coins in range(min(len(piles[i - 1]), coins) + 1):
                    if current_coins > 0:
                        current_sum += piles[i - 1][current_coins - 1]
                    dp[i][coins] = max(dp[i][coins],
                                       dp[i - 1][coins - current_coins] + current_sum)
        return dp[-1][-1]


if __name__ == "__main__":
    assert Solution().maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2) == 101
    assert Solution().maxValueOfCoins(piles=[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]],
                                      k=7) == 706
