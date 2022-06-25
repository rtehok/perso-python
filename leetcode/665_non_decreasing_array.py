from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if c == 1:
                    return False
                c += 1
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
        return True


if __name__ == "__main__":
    assert Solution().checkPossibility([4, 2, 3])
    assert not Solution().checkPossibility([4, 2, 1])
    assert not Solution().checkPossibility([3, 4, 2, 3])
