from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            sum = nums[r] + nums[l]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1


if __name__ == "__main__":
    assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [1, 2]
    assert Solution().twoSum(nums=[2, 3, 4], target=6) == [1, 3]
    assert Solution().twoSum(nums=[-1, 0], target=-1) == [1, 2]
    assert Solution().twoSum(nums=[1, 2, 3, 4, 4, 9, 56, 90], target=8) == [4, 5]
