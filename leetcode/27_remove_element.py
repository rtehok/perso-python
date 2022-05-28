from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == val:
                j = i
                while j <= len(nums) - 1 and nums[j] == val:
                    j += 1
                nums[i:] = nums[j:]
                return len(nums)


if __name__ == "__main__":
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(a, 2) == 5
    b = [3, 2, 2, 3]
    assert Solution().removeElement(b, 3) == 2
    c = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(c, 2) == 5
