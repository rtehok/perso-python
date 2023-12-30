class Solution:
    def numRollsToTargetDFS(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(n, remain):
            if target == 0 and n == 0:
                return 1
            if n == 0 or remain <= 0:
                return 0

            if dp[n][remain] != -1:
                return dp[n][remain]

            ways = 0
            for i in range(1, k + 1):
                ways = (ways + dfs(n - 1, remain - i)) % MOD

            dp[n][target] = ways
            return dp[n][remain]

        return dfs(n, target)

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [0] * (target + 1)
        curr = [0] * (target + 1)
        prev[0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                ans = 0
                for x in range(1, k + 1):
                    if j - x >= 0:
                        ans += prev[j - x] % MOD
                curr[j] = ans
            prev = curr[:]
        return prev[target] % MOD


assert Solution().numRollsToTarget(n=1, k=6, target=3) == 1
assert Solution().numRollsToTarget(n=2, k=6, target=7) == 6
assert Solution().numRollsToTarget(n=30, k=30, target=500) == 222616187
