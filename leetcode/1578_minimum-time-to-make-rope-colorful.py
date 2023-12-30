from typing import List


class Solution:
    def minCostV1(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        dp = [-1] * n

        def dfs(i, prev_color, prev_time):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            if colors[i] == prev_color:
                dp[i] = min(neededTime[i], prev_time) + dfs(i - 1, colors[i], max(neededTime[i], prev_time))
                return dp[i]
            else:
                dp[i] = dfs(i - 1, colors[i], neededTime[i])
                return dp[i]

        return dfs(n - 1, "A", neededTime[-1])

    def minCostV2(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        total_time = 0
        i, j = 0, 0
        while i < n and j < n:
            curr_total = 0
            curr_max = 0
            while j < n and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1

            total_time += curr_total - curr_max
            i = j
        return total_time

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                time += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return time


assert Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]) == 3
assert Solution().minCost(colors="abc", neededTime=[1, 2, 3]) == 0
assert Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]) == 2
