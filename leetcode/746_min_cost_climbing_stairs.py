from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp0 = cost[0]
        # dp1 = cost[1]
        #
        # for i in range(2, len(cost)):
        #     tmp = cost[i] + min(dp0, dp1)
        #     dp0 = dp1
        #     dp1 = tmp
        #
        # return min(dp0, dp1)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


if __name__ == "__main__":
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
