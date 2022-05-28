from typing import List


# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# https://leetcode.com/problems/next-permutation/solution/
# https://leetcode.com/media/original_images/31_Next_Permutation.gif
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1

        # find "last" (from the end) increasing num
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                j = i

        # if not found, reverse the all array
        if j < 0:
            nums.reverse()
            return

        # find the next in number larger than nums[j] in nums[j+1:] (which is sorted)
        k = -1
        for i in range(j + 1, len(nums)):
            if nums[i] > nums[j]:
                k = i

        # swap
        nums[j], nums[k] = nums[k], nums[j]

        # swap the sublist
        left, right = j + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    a = [1, 2, 3]
    Solution().nextPermutation(a)
    assert a == [1, 3, 2]

    a = [1, 3, 2]
    Solution().nextPermutation(a)
    assert a == [2, 1, 3]

    a = [3, 2, 1]
    Solution().nextPermutation(a)
    assert a == [1, 2, 3]

    a = [1, 1, 5]
    Solution().nextPermutation(a)
    assert a == [1, 5, 1]

    a = [1, 2, 3, 4, 5]
    Solution().nextPermutation(a)
    assert a == [1, 2, 3, 5, 4]

    a = [5, 4, 7, 5, 3, 2]
    Solution().nextPermutation(a)
    assert a == [5, 5, 2, 3, 4, 7]

    a = [0, 1, 2, 5, 3, 3, 0]
    Solution().nextPermutation(a)
    assert a == [0, 1, 3, 0, 2, 3, 5]
