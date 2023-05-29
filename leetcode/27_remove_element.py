from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n


if __name__ == "__main__":
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(a, 2) == 5
    b = [3, 2, 2, 3]
    assert Solution().removeElement(b, 3) == 2
    c = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(c, 2) == 5
