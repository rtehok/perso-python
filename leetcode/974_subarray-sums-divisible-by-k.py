import collections
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        res = 0

        cnt = collections.Counter()

        for num in nums:
            running_sum += num
            if running_sum % k == 0:
                res += 1
            res += cnt[running_sum % k]
            cnt[running_sum % k] += 1

        return res


assert Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7
assert Solution().subarraysDivByK(nums=[5], k=9) == 0
