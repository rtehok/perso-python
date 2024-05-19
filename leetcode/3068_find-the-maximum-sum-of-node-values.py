from typing import List


class Solution:
    def maximumValueSumRecursive(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        memo = [[-1] * 2 for _ in range(n)]

        def maxSumOfNodes(idx, isEven):
            if idx == len(nums):
                return 0 if isEven else float("-inf")

            if memo[idx][isEven] != -1:
                return memo[idx][isEven]

            noXorDone = nums[idx] + maxSumOfNodes(idx + 1, isEven)
            xorDone = (nums[idx] ^ k) + maxSumOfNodes(idx + 1, isEven ^ 1)
            memo[idx][isEven] = max(xorDone, noXorDone)

            return memo[idx][isEven]

        return maxSumOfNodes(0, 1)

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        dp[n][0] = float("-inf")

        for idx in range(n - 1, -1, -1):
            for isEven in range(2):
                xorDone = dp[idx + 1][isEven ^ 1] + (nums[idx] ^ k)
                noXorDone = dp[idx + 1][isEven] + nums[idx]

                dp[idx][isEven] = max(xorDone, noXorDone)

        return dp[0][1]


assert Solution().maximumValueSum(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]) == 6
assert Solution().maximumValueSum(nums=[2, 3], k=7, edges=[[0, 1]]) == 9
assert Solution().maximumValueSum(nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == 42
