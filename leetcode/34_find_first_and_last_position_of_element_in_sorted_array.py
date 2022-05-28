from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                left, right = mid, mid
                while left >= 0 and nums[mid] == nums[left]:
                    left -= 1
                while right <= len(nums) - 1 and nums[mid] == nums[right]:
                    right += 1
                return [left + 1, right - 1]

        return [-1, -1]


if __name__ == "__main__":
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([], 0) == [-1, -1]
