from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res


if __name__ == "__main__":
    assert Solution().singleNumber([2, 2, 1]) == 1
    #   100    4
    # ^ 001  + 1
    # -----
    #   101
    # ^ 010  + 2
    # -----
    #   111
    # ^ 001  - 1
    # -----
    #   110
    # ^ 010  - 2
    # -----
    #   100
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber([1]) == 1
