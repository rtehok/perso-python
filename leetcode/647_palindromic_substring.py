class Solution:
    def countSubstrings(self, s: str) -> int:
        # # dp[i][j] == True if s[i:j+1] is palindrome
        # dp = [[False] * len(s) for _ in range(len(s))]
        #
        # cnt = 0
        #
        # for i in range(len(s)):
        #     dp[i][i] = True
        #     cnt += 1
        #
        # # extends from i going left and right
        # for i in range(len(s) - 2, -1, -1):
        #     for j in range(i + 1, len(s)):
        #         if s[i] == s[j]:
        #             # j - i = 1 ==> 2 identical chars
        #             # dp[i + 1][j - 1] == s[i+1:j] is a palindrome, i.e. a???a is a palindrome
        #             if j - i == 1 or dp[i + 1][j - 1]:
        #                 dp[i][j] = True
        #                 cnt += 1
        #
        # return cnt

        def countPalindrome(l, r):
            res = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            return res

        res = 0

        for i in range(len(s)):
            r = l = i
            res += countPalindrome(l, r)

        for i in range(len(s)):
            l = i
            r = i + 1
            res += countPalindrome(l, r)

        return res


if __name__ == "__main__":
    print(Solution().countSubstrings("abc"))
    print(Solution().countSubstrings("aaa"))
    print(Solution().countSubstrings("aaba"))
    print(Solution().countSubstrings("aadcddqqaaa"))
