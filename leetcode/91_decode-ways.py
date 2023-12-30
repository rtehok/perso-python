class Solution:
    def numDecodingsTopDown(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]

            ans = dfs(i + 1)
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                ans += dfs(i + 2)
            memo[i] = ans

            return ans

        return dfs(0)

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i + 1 < n and int(s[i: i + 2]) <= 26:
                    dp[i] += dp[i + 2]
        return dp[0]


assert Solution().numDecodings("12") == 2
assert Solution().numDecodings("226") == 3
assert Solution().numDecodings("06") == 0
