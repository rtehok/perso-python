import functools


class Solution:
    def numOfArraysTopDown(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.cache
        def dp(i, max_so_far, remain):
            if i == n:  # filled the array
                if remain == 0:
                    return 1
                return 0

            # calculate max_so_far * nb of ways to add range [i ... max_so_far] (no new maximums)
            # + nb of ways to add range [max_so_far ... m] (new maximums)
            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD  # take to the max_so_far value
            for num in range(max_so_far + 1, m + 1):  # take from max_so_far to m
                ans = (ans + dp(i + 1, num, remain - 1)) % MOD

            return ans

        return dp(0, 0, k)

    def numOfArraysBottomUp(self, n: int, m: int, k: int) -> int:
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        MOD = 10 ** 9 + 7

        for num in range(len(dp[0])):
            dp[n][num][0] = 1  # base case in top-down approach

        for i in range(n - 1, -1, -1):
            for max_so_far in range(m, -1, -1):
                for remain in range(k + 1):
                    ans = (max_so_far * dp[i + 1][max_so_far][remain]) % MOD

                    if remain > 0:
                        for num in range(max_so_far + 1, m + 1):
                            ans = (ans + dp[i + 1][num][remain - 1]) % MOD

                    dp[i][max_so_far][remain] = ans

        return dp[0][0][k]

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        prev_dp = [[0] * (k + 1) for _ in range(m + 1)]

        MOD = 10 ** 9 + 7

        for num in range(len(prev_dp)):
            prev_dp[num][0] = 1  # base case in top-down approach

        for i in range(n - 1, -1, -1):
            dp = [[0] * (k + 1) for _ in range(m + 1)]  # Reset dp
            for max_so_far in range(m, -1, -1):
                for remain in range(k + 1):
                    ans = (max_so_far * prev_dp[max_so_far][remain]) % MOD

                    if remain > 0:
                        for num in range(max_so_far + 1, m + 1):
                            ans = (ans + prev_dp[num][remain - 1]) % MOD

                    dp[max_so_far][remain] = ans

            prev_dp = dp

        return dp[0][k]


if __name__ == "__main__":
    assert Solution().numOfArrays(n=2, m=3, k=1) == 6
    assert Solution().numOfArrays(n=5, m=2, k=3) == 0
