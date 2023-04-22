from functools import cache


class Solution:
    def minInsertionsRecursive(self, s: str) -> int:
        @cache
        def min_insertions(l, r):
            if l >= r:
                return 0
            elif s[l] == s[r]:
                return min_insertions(l + 1, r - 1)
            else:
                return min(min_insertions(l + 1, r), min_insertions(l, r - 1)) + 1

        return min_insertions(0, len(s) - 1)

    def minInsertionsDP(self, s: str) -> str:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def min_insertions(l, r):
            if l >= r:
                return 0
            if memo[l][r] != -1:
                return memo[l][r]
            if s[l] == s[r]:
                memo[l][r] = min_insertions(l + 1, r - 1)
            else:
                memo[l][r] = min(min_insertions(l + 1, r), min_insertions(l, r - 1)) + 1
            return memo[l][r]

        return min_insertions(0, n - 1)

    def minInsertions(self, s: str) -> int:
        n = len(s)
        # dp[i][j] represents the minimum number of insertions needed to make the substring s[i...j] a palindrome
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:  # no need to add
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

        return dp[0][-1]


if __name__ == "__main__":
    assert Solution().minInsertions("mbadm") == 2
    assert Solution().minInsertions("zzazz") == 0
    assert Solution().minInsertions("leetcode") == 5
