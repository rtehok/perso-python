from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(index: int):
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                solve(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        solve(0)

        return res


if __name__ == "__main__":
    assert Solution().permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    assert Solution().permute([0, 1]) == [[0, 1], [1, 0]]
    assert Solution().permute([1]) == [[1]]
