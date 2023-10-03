import collections
from typing import List


class Solution:
    def numIdenticalPairsV1(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    res += 1
        return res

    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        cnt = collections.defaultdict(int)
        for num in nums:
            res += cnt[num]
            cnt[num] += 1

        return res


if __name__ == "__main__":
    assert Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert Solution().numIdenticalPairs([1, 1, 1, 1]) == 6
    assert Solution().numIdenticalPairs([1, 2, 3]) == 0
