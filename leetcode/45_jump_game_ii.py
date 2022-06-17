from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        dp[-1] = 0
        dp[-2] = 1

        if n == 1:
            return 0
        if nums[0] >= len(nums):
            return 1

        for i in range(n - 2, 0, -1):
            v = nums[i - 1]
            if v >= n - 1 - (i - 1):
                # can jump from i - 1
                dp[i - 1] = 1
            elif v == 0:
                # needs to jump from i - 1 to the end
                dp[i - 1] = n - 1
            else:
                # need to store min from previous steps all the way to i + v
                dp[i - 1] = min(dp[i:i + v]) + 1

        return dp[0]


if __name__ == "__main__":
    assert Solution().jump([2, 3, 1, 1, 4, 0]) == 3
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
