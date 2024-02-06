from typing import List


class Solution:
    def maxSumAfterPartitioningRecursive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        memo = [-1] * n

        def maxSum(start):
            if start == n:
                return 0

            if memo[start] != -1:
                return memo[start]

            curr_max = 0
            ans = 0
            end = min(n, start + k)
            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                ans = max(ans, curr_max * (i - start + 1) + maxSum(i + 1))
            memo[start] = ans
            return ans

        return maxSum(0)

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            curr_max = 0
            end = min(n, start + k)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start] = max(dp[start], dp[i + 1] + curr_max * (i - start + 1))

        return dp[0]


assert Solution().maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3) == 84
assert Solution().maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4) == 83
