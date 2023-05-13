class Solution:
    def countGoodStringsDP(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)  # nb of good strings of length i
        dp[0] = 1  # empty string has only one good string of length 0

        for end in range(1, high + 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= MOD
        return sum(dp[low:high + 1]) % MOD

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [-1] * high
        MOD = 10 ** 9 + 7

        def dfs(end):
            if dp[end] != -1:
                return dp[end]

            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)

            dp[end] = count % MOD

            return dp[end]

        return sum(dfs(end) for end in range(low, high + 1)) % MOD


if __name__ == "__main__":
    assert Solution().countGoodStrings(low=3, high=3, zero=1, one=1) == 8
    assert Solution().countGoodStrings(low=2, high=3, zero=1, one=2) == 5
