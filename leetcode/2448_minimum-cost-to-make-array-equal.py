from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num_and_cost = sorted([[num, c] for num, c in zip(nums, cost)])
        n = len(nums)
        mid = sum(nums) // n

        prefix_cost = [0] * n
        prefix_cost[0] = num_and_cost[0][1]

        for i in range(1, n):
            prefix_cost[i] = num_and_cost[i][1] + prefix_cost[i - 1]

        total_cost = 0

        # start at 0
        for i in range(1, n):
            total_cost += num_and_cost[i][1] * (num_and_cost[i][0] - num_and_cost[0][0])

        res = total_cost

        for i in range(1, n):
            gap = num_and_cost[i][0] - num_and_cost[i - 1][0]
            total_cost += prefix_cost[i - 1] * gap
            total_cost -= gap * (prefix_cost[-1] - prefix_cost[i - 1])
            res = min(res, total_cost)

        return res


if __name__ == "__main__":
    assert Solution().minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]) == 8
    assert Solution().minCost(nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]) == 0
