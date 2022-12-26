from typing import List


class Solution:
    def canJumpRecursive(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        for i in reversed(range(n - 1)):
            if i + nums[i] >= n - 1:
                return self.canJump(nums[0:i + 1])

        return False

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        left = n - 1  # leftmost element that can be reached

        for i in range(n - 2, -1, -1):
            # nums[i] >= n - i - 1 ==> you can jump to the end
            # nums[i] >= left - i ==> you can jump to the next index (on the left) that can reach the end
            if nums[i] >= n - i - 1 or nums[i] >= left - i:
                left = i

        return left == 0


if __name__ == "__main__":
    assert Solution().canJump([2, 3, 1, 1, 4])
    assert not Solution().canJump([3, 2, 1, 0, 4])
    assert Solution().canJump([2, 0, 0])
    assert Solution().canJump([2, 0])
    assert Solution().canJump([2, 5, 0, 0])
    assert Solution().canJump([1, 1, 1, 0])
