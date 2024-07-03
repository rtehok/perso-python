from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()

        """
        1234567
        ---     remove 123 , diff 7 - 4
            --- remove 567 , diff 4 - 1
        -    -- remove 1 67, diff 5 - 2
        --    - remove 12 7, diff 6 - 3
        """

        return min(
            nums[-1] - nums[3],
            nums[-4] - nums[0],
            nums[-3] - nums[1],
            nums[-2] - nums[2]
        )


assert Solution().minDifference([5, 3, 2, 4]) == 0
assert Solution().minDifference([1, 5, 0, 10, 14]) == 1
assert Solution().minDifference([3, 100, 20]) == 0