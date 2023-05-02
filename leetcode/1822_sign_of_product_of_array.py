from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num == 0:
                return 0
            res *= num

        return -1 if res < 0 else 1


if __name__ == "__main__":
    assert Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert Solution().arraySign([1, 5, 0, 2, -3]) == 0
    assert Solution().arraySign([-1, 1, -1, 1, -1]) == -1
