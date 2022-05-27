import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = math.inf
        N = len(nums)

        nums.sort()

        for i in range(N - 2):
            l, r = i + 1, N - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if target >= sum:
                    l += 1
                elif target < sum:
                    r -= 1
                if abs(target - sum) < abs(closest):
                    closest = target - sum

        return target - closest


if __name__ == "__main__":
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
