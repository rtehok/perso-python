from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        total_count = 0

        left = 0
        product = 1
        for right, num in enumerate(nums):
            while product >= k:
                product //= nums[left]
                left += 1

            total_count += right - left + 1

        return total_count


assert Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100) == 8
assert Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0) == 0
