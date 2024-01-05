import collections
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        ans = 0
        for c in cnt.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans


assert Solution().minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
assert Solution().minOperations([2, 1, 2, 2, 3, 3]) == -1
