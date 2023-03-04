from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_position, max_position, left_bound = -1, -1, -1

        for i, number in enumerate(nums):
            # if number is outside of range, update left_bound
            if number < minK or number > maxK:
                left_bound = i

            # update most recent positions
            if number == minK:
                min_position = i
            if number == maxK:
                max_position = i

            res += max(0, min(min_position, max_position) - left_bound)

        return res


if __name__ == "__main__":
    assert Solution().countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5) == 2
    assert Solution().countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1) == 10
    assert Solution().countSubarrays(
        [35054, 398719, 945315, 945315, 820417, 945315, 35054, 945315,
         171832, 945315, 35054, 109750, 790964, 441974, 552913], 35054, 945315) == 81
