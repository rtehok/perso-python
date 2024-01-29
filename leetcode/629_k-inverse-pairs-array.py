class Solution:
    def kInversePairsTLE(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def solve(i, j):
            if i == 0:
                return 0  # at the end of the array
            if j == 0:
                return 1  # found k pair -> add 1 to counter

            if dp[i][j] != -1:
                return dp[i][j]

            cnt = 0
            for x in range(min(i - 1, j) + 1):  # take min to arrive at base case rapidly
                cnt += solve(i - 1, j - x)  # create all permutation of k - 0 to k - k
                cnt %= MOD
                dp[i][j] = cnt
            return cnt

        return solve(n, k)

    def kInversePairsBottomUpTLE(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1  # base case in previous scenario
                    continue
                for x in range(min(i - 1, j) + 1):
                    dp[i][j] += dp[i - 1][j - x]
                    dp[i][j] %= MOD
        return dp[-1][-1]

    def kInversePairs(self, N: int, K: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        for n in range(1, N + 1):
            for k in range(K + 1):
                if k == 0:
                    dp[n][k] = 1  # base case in previous scenario
                    continue
                dp[n][k] = (dp[n - 1][k] + dp[n][k - 1]) % MOD
                if k >= n:
                    dp[n][k] = (dp[n][k] - dp[n - 1][k - n]) % MOD
        return dp[-1][-1]


assert Solution().kInversePairs(n=3, k=0) == 1
assert Solution().kInversePairs(n=3, k=1) == 2
