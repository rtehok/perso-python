from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if j > 0 and nums[j] != nums[j - 1]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    a = [1, 1, 2]
    assert Solution().removeDuplicates(a) == 2
    assert a[:2] == [1, 2]
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().removeDuplicates(a) == 5
    assert a[:5] == [0, 1, 2, 3, 4]
