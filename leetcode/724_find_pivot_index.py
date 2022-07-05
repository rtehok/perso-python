from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        #
        # return -1
        S = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (S - left_sum - num):
                return i
            left_sum += num

        return -1


if __name__ == "__main__":
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert Solution().pivotIndex([1, 2, 3]) == -1
    assert Solution().pivotIndex([2, 1, -1]) == 0
