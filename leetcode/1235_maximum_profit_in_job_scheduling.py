import bisect
from bisect import bisect_left
from typing import List


class Solution:
    def jobSchedulingV1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [[0, 0]]  # contains [end time, max profit]

        # bisect_left(arr, x) gives the closest (on the left) value to x in array
        # look for previous valid job for x (either end or start)
        f = lambda x: dp[bisect_left(dp, [x + 1]) - 1][1]

        for (e, s, p) in sorted(zip(endTime, startTime, profit)):
            dp.append([e, max(f(e), f(s) + p)])
            # 0/1 knapsack:
            # include: take the profit of the current job + previous valid job
            # exclude: f(e) stays the same

        return dp[-1][1]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        nb_of_jobs = len(profit)
        dp = [0] * (nb_of_jobs + 1)

        for i, (e, s, p) in enumerate(jobs):
            index = bisect.bisect_right(jobs, s, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + p)

        return dp[-1]


if __name__ == "__main__":
    assert Solution().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9],
                                    profit=[20, 20, 100, 70, 60]) == 150
    #  ––-–  ––-–  ––-–  ––––––––––––––––-–
    #    3     1    20   [[0,0],[3,20]]
    #    5     2    20   [[0,0],[3,20],[5,20]]
    #    6     4    70   [[0,0],[3,20],[5,20],[6,90]]
    #    9     6    60   [[0,0],[3,20],[5,20],[6,90],[9,150]]
    #   10     3   100   [[0,0],[3,20],[5,20],[6,90],[9,150],[10,150]]
    #                                                             |
    #                                                           answer
    assert Solution().jobScheduling([1, 2, 3, 3],
                                    [3, 4, 5, 6],
                                    [50, 10, 40, 70]) == 120
    assert Solution().jobScheduling([1, 2, 2, 3],
                                    [2, 5, 3, 4],
                                    [3, 4, 1, 2]) == 7
