from typing import List


class Solution:
    def combinationSum4TopDown(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(remainder):
            if remainder == 0:
                return 1

            if remainder in memo:
                return memo[remainder]

            ans = 0
            for num in nums:
                if remainder - num >= 0:
                    ans += dfs(remainder - num)
                memo[remainder] = ans
            return memo[remainder]

        return dfs(target)

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)  # dp[i] = number of combination that sum up to i
        dp[0] = 1  # there is one way to produce a combination of target 0 with 0 element

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]


if __name__ == "__main__":
    assert Solution().combinationSum4(nums=[1, 2, 3], target=4) == 7
    assert Solution().combinationSum4(nums=[9], target=3) == 0
