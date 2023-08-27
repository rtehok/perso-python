from typing import List


class Solution:
    def findLongestChainTopDown(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            memo[i] = 1
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    memo[i] = max(memo[i], dfs(j) + 1)

            return memo[i]

        res = 0
        for i in range(n):
            res = max(res, dfs(i))

        return res

    def findLongestChainBottomUp(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1] * n

        ans = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])

        return ans

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr = float("-inf")
        ans = 0
        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]
        return ans


if __name__ == "__main__":
    assert Solution().findLongestChain(pairs=[[1, 2], [2, 3], [3, 4]]) == 2
    assert Solution().findLongestChain(pairs=[[1, 2], [7, 8], [4, 5]]) == 3
