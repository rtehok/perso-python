from typing import List


class Solution:
    def minCostDP(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)
        # dp[i][j] represents the minimum cost to cut the stick from position i to position j
        dp = [[float("inf")] * m for _ in range(m)]

        for left in range(m - 2, -1, -1):
            for right in range(left + 1, m):
                if right - left == 1:
                    dp[left][right] = 0  # no cost for cutting an adjacent position
                else:
                    for cut in range(left + 1, right):
                        dp[left][right] = min(dp[left][right], dp[left][cut] + dp[cut][right] + cuts[right] - cuts[left])

        return dp[0][-1]

    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cuts = [0] + sorted(cuts) + [n]

        def cost(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if right - left == 1:
                return 0

            ans = min(cost(left, mid) + cost(mid, right) + cuts[right] - cuts[left] for mid in range(left + 1, right))
            memo[(left, right)] = ans

            return ans

        return cost(0, len(cuts) - 1)


if __name__ == "__main__":
    assert Solution().minCost(n=7, cuts=[1, 3, 4, 5]) == 16
    # 7 + 6 + 4 + 3 = 20 (in cut in ascending order)
    # 7 + 4 + 3 + 2 = 16 (cut in 3, 5, 1, 4 order)
    assert Solution().minCost(n=9, cuts=[5, 6, 1, 4, 2]) == 22
