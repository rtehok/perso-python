from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue

            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            res += num_elements - 1

            nums[i] = nums[i] // num_elements
        return res


if __name__ == "__main__":
    assert Solution().minimumReplacement(nums=[3, 9, 3]) == 2
    assert Solution().minimumReplacement(nums=[1, 2, 3, 4, 5]) == 0
