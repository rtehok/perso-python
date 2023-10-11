from bisect import bisect_right
from typing import List


class Solution:
    def minOperationsBinarySearch(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1  # create an array of length n
            j = bisect_right(new_nums, right)  # search index of leftmost element that is close to right
            count = j - i  # number of changes to be made

            ans = min(ans, n - count)

        return ans

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0

        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1

            count = j - i
            ans = min(ans, n - count)

        return ans


if __name__ == "__main__":
    assert Solution().minOperations(nums=[4, 2, 5, 3]) == 0
    assert Solution().minOperations(nums=[1, 2, 3, 5, 6]) == 1
    assert Solution().minOperations(nums=[1, 10, 100, 1000]) == 3
