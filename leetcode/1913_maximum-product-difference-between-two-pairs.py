from typing import List


class Solution:
    def maxProductDifferenceSort(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

    def maxProductDifference(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        smallest = float("inf")
        second_smallest = float("inf")
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
            if num < smallest:
                second_smallest = smallest
                smallest = num
            else:
                second_smallest = min(second_smallest, num)
        return biggest * second_biggest - smallest * second_smallest


assert Solution().maxProductDifference([5, 6, 2, 7, 4]) == 34
assert Solution().maxProductDifference([4, 2, 5, 9, 7, 4, 8]) == 64
