from math import comb
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1

            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]

            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % MOD

        return (dfs(nums) - 1) % MOD


if __name__ == "__main__":
    assert Solution().numOfWays([2, 1, 3]) == 1
    assert Solution().numOfWays([3, 4, 5, 1, 2]) == 5
    assert Solution().numOfWays([1, 2, 3]) == 0
