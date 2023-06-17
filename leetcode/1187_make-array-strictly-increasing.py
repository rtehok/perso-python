import bisect
import collections
from typing import List


class Solution:
    # TC O(n * m * log(m)) / SC O(m * n)
    def makeArrayIncreasingDFS(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        memo = {}

        n = len(arr1)
        m = len(arr2)

        def dfs(i, prev):
            if i == n:
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            cost = float("inf")

            if arr1[i] > prev:  # leave it as-is
                cost = dfs(i + 1, arr1[i])

            idx = bisect.bisect_right(arr2, prev)

            if idx < m:
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            memo[(i, prev)] = cost

            return cost

        res = dfs(0, -1)

        return -1 if res == float("inf") else res

    # TC O(n * m * log(m)) / SC O(n)
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr2)
        dp = {-1: 0}

        for i in range(len(arr1)):
            new_dp = collections.defaultdict(lambda: float("inf"))
            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect.bisect_right(arr2, prev)

                if idx < n:
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])

            dp = new_dp

        return min(dp.values()) if dp else - 1


if __name__ == "__main__":
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]) == 1
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]) == 2
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]) == -1
