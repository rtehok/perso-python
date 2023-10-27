class Solution:
    def longestPalindromeV1(self, s: str) -> str:
        self.start = 0
        self.length = 0

        def findStartAndLength(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if self.length < r - l + 1:
                    self.start = l
                    self.length = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            findStartAndLength(i, i)
            findStartAndLength(i, i + 1)

        return s[self.start:self.start + self.length]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]


if __name__ == "__main__":
    assert Solution().longestPalindrome("babad") == "aba"
    assert Solution().longestPalindrome("cbbd") == "bb"
