import math
from typing import List


class Solution:
    def stoneGameIIV1(self, piles: List[int]) -> int:
        n = len(piles)

        # player == 0 == Alice, i is the state == piles[i] is considered the first pile, m is as described
        def helper(player, i, m):
            if i == n:
                return 0

            res = math.inf if player == 1 else -math.inf
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if player == 0:
                    res = max(res, s + helper(1, i + x, max(m, x)))
                else:
                    res = min(res, helper(0, i + x, max(m, x)))  # bob wants to minimize Alice result

            return res

        return helper(0, 0, 1)

    def stoneGameIIDP(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[-1] * (n + 1) for i in range(n + 1)] for p in (0, 1)]

        def helper(player, i, m):
            if i == n:
                return 0

            if dp[player][i][m] != -1:
                return dp[player][i][m]

            res = math.inf if player == 1 else -math.inf
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if player == 0:
                    res = max(res, s + helper(1, i + x, max(m, x)))
                else:
                    res = min(res, helper(0, i + x, max(m, x)))  # bob wants to minimize Alice result

            dp[player][i][m] = res
            return res

        return helper(0, 0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        def helper(i, m):  # function to maximize score
            if i == n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]

            if dp[i][m] != 0:
                return dp[i][m]

            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - helper(i + x, max(m, x)))
            dp[i][m] = res
            return res

        return helper(0, 1)


if __name__ == "__main__":
    assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10
    assert Solution().stoneGameII([1, 2, 3, 4, 5, 100]) == 104
