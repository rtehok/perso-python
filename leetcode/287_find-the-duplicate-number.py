from typing import List


class Solution:
    def findDuplicateTLE(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]

        return -1

    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def findDuplicateBitManip(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = 0

        for i in range(1, n + 1):
            res ^= i

        for num in nums:
            res ^= num

        return res


if __name__ == "__main__":
    assert Solution().findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
