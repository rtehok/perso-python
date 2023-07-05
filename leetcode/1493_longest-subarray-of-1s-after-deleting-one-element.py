from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = 0
        longest_window = 0

        left = 0
        for right in range(n):
            zeros += nums[right] == 0
            while zeros > 1:
                zeros -= nums[left] == 0
                left += 1

            longest_window = max(longest_window, right - left)

        return longest_window


if __name__ == "__main__":
    assert Solution().longestSubarray([1, 1, 0, 1]) == 3
    assert Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
