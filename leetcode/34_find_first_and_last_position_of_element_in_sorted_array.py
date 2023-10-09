from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = right = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]


if __name__ == "__main__":
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([], 0) == [-1, -1]
