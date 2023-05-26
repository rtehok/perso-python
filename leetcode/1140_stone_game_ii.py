import math
from typing import List


class Solution:
    def stoneGameIIV1(self, piles: List[int]) -> int:
        n = len(piles)

        # player == 0 == Alice, i is the state == piles[i] is considered the first pile, m is as described
        def helper(player, i, m):
            if i == n:
                return 0

            cumulative_sum = math.inf if player == 1 else -math.inf
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if player == 0:
                    cumulative_sum = max(cumulative_sum, s + helper(1, i + x, max(m, x)))
                else:
                    cumulative_sum = min(cumulative_sum,
                                         helper(0, i + x, max(m, x)))  # bob wants to minimize Alice result

            return cumulative_sum

        return helper(0, 0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[-1] * (n + 1) for i in range(n + 1)] for p in (0, 1)]

        def helper(player, i, m):
            if i == n:
                return 0

            if dp[player][i][m] != -1:
                return dp[player][i][m]

            cumulative_sum = math.inf if player == 1 else -math.inf
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if player == 0:
                    cumulative_sum = max(cumulative_sum, s + helper(1, i + x, max(m, x)))
                else:
                    cumulative_sum = min(cumulative_sum,
                                         helper(0, i + x, max(m, x)))  # bob wants to minimize Alice result

            dp[player][i][m] = cumulative_sum
            return cumulative_sum

        return helper(0, 0, 1)


if __name__ == "__main__":
    assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10
    assert Solution().stoneGameII([1, 2, 3, 4, 5, 100]) == 104
