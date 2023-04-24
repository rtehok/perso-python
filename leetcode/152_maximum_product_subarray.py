import math
from typing import List


class Solution:
    def maxProductBruteForce(self, nums: List[int]) -> int:
        res = -math.inf
        n = len(nums)
        for i, num in enumerate(nums):
            tmp = num
            res = max(res, tmp)
            for j in range(i + 1, n):
                tmp *= nums[j]
                res = max(res, tmp)

        return res

    def maxProductDP(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        res = nums[0]

        for i in range(1, n):
            if nums[i] == 0:
                max_dp[i] = min_dp[i] = 0
            elif nums[i] > 0:
                max_dp[i] = max(nums[i], nums[i] * max_dp[i - 1])
                min_dp[i] = min(nums[i], nums[i] * min_dp[i - 1])
            else:
                max_dp[i] = max(nums[i], nums[i] * min_dp[i - 1])
                min_dp[i] = min(nums[i], nums[i] * max_dp[i - 1])

            res = max(res, max_dp[i])

        return res

    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            temp = max_so_far
            max_so_far = max(nums[i], max(max_so_far * nums[i], min_so_far * nums[i]))
            min_so_far = min(nums[i], min(temp * nums[i], min_so_far * nums[i]))
            max_product = max(max_product, max_so_far)

        return max_product


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
    assert Solution().maxProduct([-2]) == -2
    assert Solution().maxProduct([-2, 0, -1]) == 0
