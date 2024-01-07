import collections
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0

        dp = [collections.defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]

                if diff > 2 ** 31 - 1 or diff < -2 ** 31:
                    continue

                count = dp[j][diff]

                total_count += count
                dp[i][diff] += count + 1

        return total_count


assert Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7
assert Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]) == 16
