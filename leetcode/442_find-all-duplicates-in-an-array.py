from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        n = len(nums)
        i = 0
        while i < n:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates


assert Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [3, 2]
assert Solution().findDuplicates([1, 1, 2]) == [1]
assert Solution().findDuplicates([1]) == []
