class Solution:
    def longestPalindrome(self, s: str) -> str:
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


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
