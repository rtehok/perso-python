from typing import List


class Solution:
    def longestSubsequenceBruteForce(self, arr: List[int], difference: int) -> int:
        ans = 1
        n = len(arr)
        for i in range(n):
            factor = 0
            for j in range(i, n):
                if arr[j] == arr[i] + difference * factor:
                    factor += 1
                    continue
            ans = max(ans, factor)

        return ans

    def longestSubsequenceDFS(self, arr: List[int], difference: int) -> int:
        d = {}

        def dfs(i):
            if i == len(arr):
                return d[arr[i - 1]]
            if arr[i] - difference in d:
                d[arr[i]] = d[arr[i] - difference] + 1
            else:
                d[arr[i]] = 1
            return max(d[arr[i]], dfs(i + 1))

        return dfs(0)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1

        for a in arr:
            dp[a] = dp.get(a - difference, 0) + 1
            ans = max(ans, dp[a])

        return ans


if __name__ == "__main__":
    assert Solution().longestSubsequence(arr=[1, 2, 3, 4], difference=1) == 4
    assert Solution().longestSubsequence(arr=[1, 3, 5, 7], difference=1) == 1
    assert Solution().longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2) == 4
