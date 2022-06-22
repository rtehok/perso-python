from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted(map(lambda x: x * x, nums))
        i, j = 0, len(nums) - 1
        res = []
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                res.insert(0, nums[j] ** 2)
                j -= 1
            else:
                res.insert(0, nums[i] ** 2)
                i += 1
        return res


if __name__ == "__main__":
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
