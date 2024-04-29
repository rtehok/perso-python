from functools import reduce
from operator import xor
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(xor, nums, k).bit_count()


assert Solution().minOperations(nums=[2, 1, 3, 4], k=1) == 2
assert Solution().minOperations(nums=[2, 0, 2, 0], k=0) == 0
