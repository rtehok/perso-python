from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target_sum = sum(nums) - x

        if target_sum == 0:
            return n

        left = current_sum = max_len = 0

        # find the maximum subarray that matches target = total_sum - x
        for right in range(n):
            current_sum += nums[right]

            while left <= right and current_sum > target_sum:
                current_sum -= nums[left]
                left += 1

            if current_sum == target_sum:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len else -1


if __name__ == "__main__":
    assert Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10) == 5
    assert Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2
    assert Solution().minOperations(nums=[5, 6, 7, 8, 9], x=4) == -1
