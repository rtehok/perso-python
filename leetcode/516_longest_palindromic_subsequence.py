class Solution:
    # SC O(n2) / TC (n2)
    def longestPalindromeSubseqRecursive(self, s: str) -> int:
        n = len(s)
        memo = {}

        def helper(l, r):
            if (l, r) in memo:
                return memo[(l, r)]

            if l > r:  # even
                return 0
            if l == r:  # odd
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = helper(l + 1, r - 1) + 2  # add 2 chars
            else:
                memo[(l, r)] = max(helper(l, r - 1), helper(l + 1, r))

            return memo[(l, r)]

        return helper(0, n - 1)

    # bottom-up
    # SC O(n2) / TC (n2)
    def longestPalindromeSubseqDP(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n - 1]

    # space optimized
    # SC O(n) / TC (n2)
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp, dp_prev = [0] * n, [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[j] = dp_prev[j - 1] + 2
                else:
                    dp[j] = max(dp[j - 1], dp_prev[j])
            dp_prev = dp[:]

        return dp[n - 1]


if __name__ == "__main__":
    assert Solution().longestPalindromeSubseq(s="bbbab") == 4
    assert Solution().longestPalindromeSubseq(s="abab") == 3
    assert Solution().longestPalindromeSubseq(s="aaaa") == 4
    assert Solution().longestPalindromeSubseq(s="aaa") == 3
    assert Solution().longestPalindromeSubseq(s="aa") == 2
    assert Solution().longestPalindromeSubseq(s="cbbd") == 2
