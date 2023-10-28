import functools


class Solution:
    def countVowelPermutationTabulation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 5 for _ in range(n)]

        for i in range(5):
            dp[0][i] = 1

        # Each vowel 'a' may only be followed by an 'e'.
        # Each vowel 'e' may only be followed by an 'a' or an 'i'.
        # Each vowel 'i' may not be followed by another 'i'.
        # Each vowel 'o' may only be followed by an 'i' or a 'u'.
        # Each vowel 'u' may only be followed by an 'a'.

        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD  # a can follow e, i, u
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD  # e can follow a and i
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD  # i can follow e and o
            dp[i][3] = dp[i - 1][2] % MOD  # o can follow i
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD  # u can follow i or o

        return sum(dp[-1]) % MOD

    def countVowelPermutationSpaceOptimized(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1

        for _ in range(1, n):
            new_a = (e + i + u) % MOD
            new_e = (a + i) % MOD
            new_i = (e + o) % MOD
            new_o = i % MOD
            new_u = (i + o) % MOD

            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u

        return (a + e + i + o + u) % MOD

    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1

        for _ in range(1, n):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i % MOD, (i + o) % MOD

        return (a + e + i + o + u) % MOD


if __name__ == "__main__":
    assert Solution().countVowelPermutation(1) == 5
    assert Solution().countVowelPermutation(2) == 10
    assert Solution().countVowelPermutation(5) == 68
    assert Solution().countVowelPermutation(144) == 18208803
