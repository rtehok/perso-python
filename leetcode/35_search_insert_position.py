from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l != r:
            mid = r - (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = max(mid - 1, l)
            else:
                l = min(mid + 1, r)

        return r + 1 if nums[r] < target else r


if __name__ == "__main__":
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
