from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()

        max_sum = 0
        curr_sum = 0
        left = 0

        for num in nums:
            while num in seen:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(num)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum


if __name__ == "__main__":
    assert Solution().maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17
    assert Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
    assert Solution().maximumUniqueSubarray([4, 2, 1, 2, 6]) == 9
    assert Solution().maximumUniqueSubarray(
        [187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266, 987, 965, 429, 166,
         809, 340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189, 169, 743, 78, 810, 70, 382, 367, 490, 787,
         670, 476, 278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]) == 16911
