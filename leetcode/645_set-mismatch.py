import collections
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = collections.Counter(nums)
        duplicated = 0
        missing = 0
        for i in range(1, n + 1):
            if i not in cnt:
                missing = i
            if cnt[i] == 2:
                duplicated = i
        return [duplicated, missing]


assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3]
assert Solution().findErrorNums([1, 1]) == [1, 2]
