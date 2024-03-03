from typing import List


class Solution:
    def sortedSquaresV1(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])

    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[r] ** 2)
                r -= 1
            else:
                res.append(nums[l] ** 2)
                l += 1
        return res[::-1]


if __name__ == "__main__":
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
