from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        days_set = set(days)
        for i in range(1, 366):
            if i not in days_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])

        return dp[days[-1]]


if __name__ == "__main__":
    assert Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]) == 11
    assert Solution().mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]) == 17
    assert Solution().mincostTickets(days=[1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28],
                                     costs=[3, 13, 45]) == 44
