from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        previous_elt_sum = 0
        ans = -1

        for num in nums:
            if num < previous_elt_sum:
                ans = num + previous_elt_sum
            previous_elt_sum += num

        return ans


assert Solution().largestPerimeter([5, 5, 5]) == 15
assert Solution().largestPerimeter([5, 5, 50]) == -1
assert Solution().largestPerimeter([1, 12, 1, 2, 5, 50, 3]) == 12
