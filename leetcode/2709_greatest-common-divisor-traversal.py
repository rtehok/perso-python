import math
from typing import List


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        if len(nums) == 1:
            return True

        # sort from high to low, then "propagate the prime factors from big numbers to smaller numbers
        nums = sorted(nums, reverse=True)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = math.gcd(nums[i], nums[j])
                if d > 1:
                    # replace nums[j] by smallest common multiple of nums[i] and nums[j]
                    nums[j] *= nums[i] // d
                    # then check the next number, we don't need to check nums[i] with other numbers anymore because the "new" nums[j] will take care of that
                    break
            else:
                # this means gcd of nums[i] to all smaller numbers is 1
                # this happens if break is not encountered in inner for loop
                return False

        return True


assert Solution().canTraverseAllPairs([2, 3, 6])
assert not Solution().canTraverseAllPairs([3, 9, 5])
assert Solution().canTraverseAllPairs([4, 3, 12, 8])
assert not Solution().canTraverseAllPairs(
    [23, 65, 30, 70, 30, 89, 30, 90, 70, 90, 50, 78, 90, 30, 30, 63, 84, 90, 100, 66, 15, 44, 84, 50, 75, 70, 3, 84, 55,
     18, 70, 60, 78, 45, 60, 15, 21, 45, 90, 84, 29, 39, 66, 77, 75, 70, 45, 70, 20, 60, 70, 42, 66, 30, 77, 78, 42, 55,
     75, 77, 60, 26, 84, 11, 45, 30, 60, 60, 70, 52, 38, 84])
