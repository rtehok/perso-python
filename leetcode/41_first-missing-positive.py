from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


assert Solution().firstMissingPositive(nums=[1, 2, 0]) == 3
assert Solution().firstMissingPositive(nums=[3, 4, -1, 1]) == 2
assert Solution().firstMissingPositive(nums=[7, 8, 9, 11, 12]) == 1
