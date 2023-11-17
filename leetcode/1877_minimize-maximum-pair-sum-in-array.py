from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1

        res = 0
        while i < j:
            res = max(res, nums[i] + nums[j])
            i += 1
            j -= 1

        return res


if __name__ == "__main__":
    assert Solution().minPairSum([3, 5, 2, 3]) == 7
    assert Solution().minPairSum([3, 5, 4, 2, 4, 6]) == 8
