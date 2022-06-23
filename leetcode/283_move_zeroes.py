from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        # while j < len(nums) and i < len(nums):
        #     if nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     elif nums[i] != 0:
        #         i += 1
        #     j += 1
        if len(nums) > 1:
            i = 0
            for j in range(1, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                while nums[i] != 0 and i < j:
                    i += 1


if __name__ == "__main__":
    a = [0, 1, 0, 12, 3]
    Solution().moveZeroes(a)
    assert a == [1, 12, 3, 0, 0]
