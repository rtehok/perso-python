from typing import List


class Solution:
    def minIncrementForUniqueSort(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        min_incr = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                incr = nums[i - 1] - nums[i] + 1
                min_incr += incr

                nums[i] = nums[i - 1] + 1

        return min_incr
        #    1 1 2 2 3 7 (original)
        # => 1 2 3 4 5 7 (changes)
        # => 0 1 1 2 2 0 (incr)

    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        min_incr = 0
        freq_count = [0] * (n + max_val + 1)
        for num in nums:
            freq_count[num] += 1

        for i in range(len(freq_count)):
            if freq_count[i] <= 1:
                continue

            duplicates = freq_count[i] - 1
            freq_count[i + 1] += duplicates
            min_incr += duplicates

        return min_incr


assert Solution().minIncrementForUnique(nums=[1, 2, 2]) == 1
assert Solution().minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]) == 6
