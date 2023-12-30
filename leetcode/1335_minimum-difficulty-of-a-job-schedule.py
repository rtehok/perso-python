import functools
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @functools.cache
        def solve(daysLeft, start):
            if daysLeft == 1:
                return max(jobDifficulty[start:])

            maxDifficulty = jobDifficulty[start]
            daysLeft -= 1
            stop = n - start - daysLeft + 1

            res = float("inf")
            for i in range(1, stop):
                maxDifficulty = max(maxDifficulty, jobDifficulty[start + i - 1])
                res = min(res, solve(daysLeft, start + i) + maxDifficulty)
            return res

        return solve(d, 0)


assert Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7
assert Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4) == -1
assert Solution().minDifficulty(jobDifficulty=[1, 1, 1], d=3) == 3
