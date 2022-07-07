class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """ Brute force """
        # if len(s1) + len(s2) != len(s3):
        #     return False
        #
        # def helper(i, j, res):
        #     if res == s3 and i == len(s1) and j == len(s2):
        #         return True
        #
        #     ans = False
        #
        #     if i < len(s1):
        #         ans |= helper(i + 1, j, f'{res}{s1[i]}')
        #     if j < len(s2):
        #         ans |= helper(i, j + 1, f'{res}{s2[j]}')
        #
        #     return ans
        #
        # return helper(0, 0, "")

        """ Brute force with memoization """
        # if len(s1) + len(s2) != len(s3):
        #     return False
        #
        # def helper(i, j, k):
        #     if i == len(s1):
        #         return s2[j:] == s3[k:]
        #
        #     if j == len(s2):
        #         return s1[i:] == s3[k:]
        #
        #     if memo[i][j] != -1:
        #         return memo[i][j]
        #
        #     ans = False
        #
        #     if (s3[k] == s1[i] and helper(i + 1, j, k + 1)) or (s3[k] == s2[j] and helper(i, j + 1, k + 1)):
        #         ans = True
        #
        #     memo[i][j] = ans
        #
        #     return ans
        #
        # memo = [[-1] * len(s2) for _ in range(len(s1))]
        #
        # return helper(0, 0, 0)

        """ DP """
        # if len(s1) + len(s2) != len(s3):
        #     return False
        #
        # # dp is empty string at (0, 0) and s1 for rows, s2 for cols
        # # dp at i and j is true if:
        # # prefix is true (for some j) (i.e. dp[i-1][j]) AND s1[i] == s3[k]  => k = i + j + 2
        # # prefix is true (for some i) (i.e. dp[i][j-1]) AND s2[j] == s3[k]  => k = i + j + 2
        # dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        #
        # for i in range(len(s1) + 1):
        #     for j in range(len(s2) + 1):
        #         if i == j == 0:
        #             dp[i][j] = True
        #         elif i == 0:
        #             dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        #         elif j == 0:
        #             dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        #         else:
        #             dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
        #                         dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])  # k == (i - 1) + j == i + (j - 1)
        #
        # return dp[-1][-1]

        """ DP space optimized """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0:
                    dp[i] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                            dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1]


if __name__ == "__main__":
    assert Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
    assert not Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
    assert Solution().isInterleave(s1="", s2="", s3="")
    assert Solution().isInterleave("aabaac", "aadaaeaaf", "aadaaeaabaafaac")
    assert not Solution().isInterleave("a", "", "c")
