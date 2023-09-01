from typing import List


class Solution:
    def minTapsDP(self, n: int, ranges: List[int]) -> int:
        dp = [float("inf")] * (n + 1)  # minimum number of tap needed to water from 0 to position i

        dp[0] = 0  # no tap needed to water garden of length 0

        for i in range(n + 1):
            tap_start = max(0, i - ranges[i])
            tap_end = min(n, i + ranges[i])

            for j in range(tap_start, tap_end + 1):
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]

    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)

        for i in range(n + 1):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])

            max_reach[start] = max(max_reach[start], end)

        taps = 0
        current_end = 0
        next_end = 0

        for i in range(n + 1):
            if i > next_end:
                return -1

            if i > current_end:
                taps += 1
                current_end = next_end

            next_end = max(next_end, max_reach[i])

        return taps


if __name__ == "__main__":
    assert Solution().minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]) == 1
    assert Solution().minTaps(n=3, ranges=[0, 0, 0, 0]) == -1
