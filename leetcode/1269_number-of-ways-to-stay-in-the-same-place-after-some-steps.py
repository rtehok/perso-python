import functools


class Solution:
    def numWaysTopDown(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        arrLen = min(steps // 2 + 1, arrLen)  # max curr <= (steps = 500), going right
        memo = [[-1] * (steps + 1) for _ in range(arrLen)]

        def solve(curr, remain):
            if remain == 0:
                if curr == 0:
                    return 1

                return 0

            if memo[curr][remain] != -1:
                return memo[curr][remain]

            ans = solve(curr, remain - 1)  # stay

            if curr > 0:
                ans = (ans + solve(curr - 1, remain - 1)) % MOD  # left

            if curr < arrLen - 1:
                ans = (ans + solve(curr + 1, remain - 1)) % MOD  # right

            memo[curr][remain] = ans

            return memo[curr][remain]

        return solve(0, steps)

    def numWaysBottomUp(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        arrLen = min(steps // 2 + 1, arrLen)
        dp = [[0] * (steps + 1) for _ in range(arrLen)]
        dp[0][0] = 1

        for remain in range(1, steps + 1):  # need to be outer loop
            for curr in range(arrLen - 1, -1, -1):
                ans = dp[curr][remain - 1]  # stay

                if curr > 0:
                    ans = (ans + dp[curr - 1][remain - 1]) % MOD  # left

                if curr < arrLen - 1:
                    ans = (ans + dp[curr + 1][remain - 1]) % MOD  # right

                dp[curr][remain] = ans

        return dp[0][steps]

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        arrLen = min(steps // 2 + 1, arrLen)
        dp = [0] * arrLen
        dp_prev = [0] * arrLen
        dp_prev[0] = 1

        for remain in range(1, steps + 1):
            dp = [0] * arrLen
            for curr in range(arrLen - 1, -1, -1):
                ans = dp_prev[curr]  # stay

                if curr > 0:
                    ans = (ans + dp_prev[curr - 1]) % MOD  # left

                if curr < arrLen - 1:
                    ans = (ans + dp_prev[curr + 1]) % MOD  # right

                dp[curr] = ans
            dp_prev = dp

        return dp[0]


if __name__ == "__main__":
    assert Solution().numWays(3, 2) == 4
    assert Solution().numWays(2, 4) == 2
