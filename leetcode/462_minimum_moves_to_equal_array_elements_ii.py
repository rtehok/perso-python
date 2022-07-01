from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        res = 0
        for i in range(len(nums)):
            res += abs(nums[i] - median)

        return res


if __name__ == "__main__":
    assert Solution().minMoves2([1, 2, 3]) == 2
    assert Solution().minMoves2([1, 10, 2, 9]) == 16
    assert Solution().minMoves2([1, 3, 2]) == 2
    assert Solution().minMoves2([1, 0, 0, 8, 6]) == 14
