from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1

        for i in range(zeros):
            nums[i] = 0

        for i in range(zeros, zeros + ones):
            nums[i] = 1

        for i in range(zeros + ones, n):
            nums[i] = 2


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
assert nums == [0, 0, 1, 1, 2, 2]
nums = [2, 0, 1]
Solution().sortColors(nums)
assert nums == [0, 1, 2]
