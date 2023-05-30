from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1

        return k


if __name__ == "__main__":
    nums = [1, 2, 3]
    assert Solution().removeDuplicates(nums) == 3
    assert nums[:3] == [1, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert Solution().removeDuplicates(nums) == 7
    assert nums[:7] == [0, 0, 1, 1, 2, 3, 3]

    nums = [1, 1, 1, 2, 2, 3]
    assert Solution().removeDuplicates(nums) == 5
    assert nums[:5] == [1, 1, 2, 2, 3]

    nums = [1, 1]
    assert Solution().removeDuplicates(nums) == 2
    assert nums[:2] == [1, 1]
