class Solution:
    def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        return dfs(0, 0)

    def longestCommonSubsequenceTab(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            next_dp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    next_dp[j] = 1 + dp[j + 1]
                else:
                    next_dp[j] = max(dp[j], next_dp[j + 1])
            dp = next_dp

        return dp[0]


if __name__ == "__main__":
    #     a b c d e   |||       a b c d e
    #   0 0 0 0 0 0   |||     0 0 0 0 0 0
    # a 0 1 1 1 1 1   |||   a 0 1 1 1 1 1
    # e 0 1 1 1 1 2   |||   c 0 1 1 2 2 2
    # c 0 1 1 1 1 2   |||   e 0 1 1 2 2 3
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0
