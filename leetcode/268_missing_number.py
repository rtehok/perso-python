from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        N = len(nums)
        for x in range(N+1):
            if x not in nums:
                return x


if __name__ == "__main__":
    assert Solution().missingNumber([3, 0, 1]) == 2
    assert Solution().missingNumber([0, 1]) == 2
    assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
