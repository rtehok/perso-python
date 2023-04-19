from typing import List


class Solution:
    def searchV1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # same bucket
            if (target < nums[0]) == (nums[mid] < nums[0]):
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    return mid
            elif target < nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # left half is sorted
                if nums[left] <= target < nums[mid]:  # is in left side
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right side is sorted
                if nums[mid] < target <= nums[right]:  # is in right side
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert Solution().search([1], 0) == -1
    assert Solution().search([5, 1, 3], 3) == 2
