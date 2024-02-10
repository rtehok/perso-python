class Solution:
    def numSquaresRecursive(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def solve(remaining):
            if dp[remaining] != -1:
                return dp[remaining]

            if remaining == 0:
                return 0

            ans = remaining
            for i in range(1, remaining):
                square = i * i
                if square > remaining:
                    break
                ans = min(ans, 1 + solve(remaining - square))

            dp[remaining] = ans
            return ans

        return solve(n)

    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for j in range(1, i):
                square = j * j
                if square > i:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]


assert Solution().numSquares(12) == 3
assert Solution().numSquares(13) == 2
