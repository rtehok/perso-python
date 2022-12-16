class Solution:
    def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:
        def helper(s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0

            if s1[i] == s2[j]:
                return 1 + helper(s1, s2, i + 1, j + 1)
            else:
                return max(helper(s1, s2, i + 1, j), helper(s1, s2, i, j + 1))

        return helper(text1, text2, 0, 0)

    def longestCommonSubsequenceSubOptimal(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if text1[col - 1] == text2[row - 1]:
                    # the one in the diagonal (add to the longest subsequence up to char in text1 AND text2)
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    # take the max in order to add + 1 if needed (the longest subsequence)
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

        return dp[n][m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        if m < n:
            return self.longestCommonSubsequence(text2, text1)

        dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[1 - i % 2][j + 1] = 1 + dp[i % 2][j]  # equivalent of the left diagonal value
                else:
                    dp[1 - i % 2][j + 1] = max(dp[1 - i % 2][j], dp[i % 2][j + 1])  # equivalent to the left and up values

        return dp[m % 2][n]


if __name__ == "__main__":
    #     a b c d e   |||       a b c d e
    #   0 0 0 0 0 0   |||     0 0 0 0 0 0
    # a 0 1 1 1 1 1   |||   a 0 1 1 1 1 1
    # e 0 1 1 1 1 2   |||   c 0 1 1 2 2 2
    # c 0 1 1 1 1 2   |||   e 0 1 1 2 2 3
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0
