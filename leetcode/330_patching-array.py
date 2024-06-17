from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        res = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1
        return res


assert Solution().minPatches(nums=[1, 3], n=6) == 1
assert Solution().minPatches(nums=[1, 5, 10], n=20) == 2
assert Solution().minPatches(nums=[1, 2, 2], n=5) == 0
