from typing import List


class Solution:
    def isMonotonicV1(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 2:
            return True

        i = 1

        prev_diff = 0

        while i < n:
            diff = nums[i] - nums[i - 1]
            if prev_diff != 0 and diff != 0 and ((prev_diff < 0 < diff) or (prev_diff > 0 > diff)):
                return False
            prev_diff = diff if diff != 0 else prev_diff
            i += 1

        return True

    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 2:
            return True

        direction = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
            elif nums[i] < nums[i - 1]:
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False

        return True


if __name__ == "__main__":
    assert Solution().isMonotonic([1, 2, 4, 5])
    assert not Solution().isMonotonic([1, 3, 2])
    assert Solution().isMonotonic([1, 2, 2, 3])
    assert Solution().isMonotonic([6, 5, 4, 4])
