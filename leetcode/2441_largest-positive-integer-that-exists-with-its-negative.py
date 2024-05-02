from typing import List


class Solution:
    def findMaxKV1(self, nums: List[int]) -> int:
        positives = reversed(sorted(x for x in nums if x > 0))
        negatives = set(-x for x in nums if x < 0)

        for p in positives:
            if p in negatives:
                return p

        return -1

    def findMaxK(self, nums: List[int]) -> int:
        ans = -1

        seen = set()

        for num in nums:
            if abs(num) > ans and -num in seen:
                ans = abs(num)

            seen.add(num)

        return ans


assert Solution().findMaxK([-1, 2, -3, 3]) == 3
assert Solution().findMaxK([-1, 10, 6, 7, -7, 1]) == 7
assert Solution().findMaxK([-10, 8, 6, 7, -2, -3]) == -1
