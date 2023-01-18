from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]

        suffix_sum = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i + 1], suffix_sum)

        max_sum = nums[0]
        special_sum = nums[0]

        prefix_sum = 0
        current_max = 0

        for i in range(n):
            current_max = max(current_max, 0) + nums[i]
            max_sum = max(max_sum, current_max)
            prefix_sum += nums[i]
            if i + 1 < n:
                special_sum = max(special_sum, prefix_sum + right_max[i + 1])
        return max(max_sum, special_sum)


if __name__ == "__main__":
    assert Solution().maxSubarraySumCircular([1, -2, 3, -2])
    assert Solution().maxSubarraySumCircular([5, -3, 5])
    assert Solution().maxSubarraySumCircular([-3, -2, -3])
