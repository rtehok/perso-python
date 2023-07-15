import bisect
from typing import List


class Solution:
    def maxValueTopDown(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        starts = [start for start, _, _ in events]
        next_indices = [bisect.bisect_right(starts, events[index][1]) for index in range(n)]

        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(index, count):
            if count == 0 or index == n:
                return 0

            if dp[count][index] != -1:
                return dp[count][index]

            next_index = next_indices[index]  # look for next available event

            dp[count][index] = max(dfs(index + 1, count),  # do not take
                                   events[index][2] + dfs(next_index, count - 1)  # take the event
                                   )

            return dp[count][index]

        return dfs(0, k)

    # Bottom-Up DP
    def maxValueBottomUp(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        starts = [start for start, _, _ in events]
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(n - 1, -1, -1):
            next_index = bisect.bisect_right(starts, events[i][1])
            for cnt in range(1, k + 1):
                dp[cnt][i] = max(dp[cnt][i + 1],
                                 events[i][2] + dp[cnt - 1][next_index])

        return dp[k][0]

    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(i, cnt, prev_ending_time):
            if i == n or cnt == k:
                return 0

            if events[i][0] <= prev_ending_time:
                return dfs(i + 1, cnt, prev_ending_time)  # skip as it is invalid

            if dp[cnt][i] != - 1:
                return dp[cnt][i]

            dp[cnt][i] = max(dfs(i + 1, cnt, prev_ending_time),  # skip
                             events[i][2] + dfs(i + 1, cnt + 1, events[i][1])  # take
                             )

            return dp[cnt][i]

        return dfs(0, 0, -1)


if __name__ == "__main__":
    assert Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2) == 7
    assert Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2) == 10
    assert Solution().maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3) == 9
