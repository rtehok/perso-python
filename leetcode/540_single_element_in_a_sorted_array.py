from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        l, r = 0, n - 1

        while l < r:
            mid = r - (r - l) // 2
            if mid % 2 == 1:  # if mid is odd, make it even, to compare with the next one
                mid -= 1

            if nums[mid] != nums[mid + 1]:  # numbers come by pair, so compares nums at mid and mid + 1 index
                r = mid  # if they are different, as you are on an even index, it must be on the left side
            else:
                l = mid + 2  # unique element is on the right side, add 2, because numbers come by pair

        return nums[l]


if __name__ == "__main__":
    assert Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
