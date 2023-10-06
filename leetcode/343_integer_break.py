import functools


class Solution:
    def integerBreakMath(self, n: int) -> int:
        if n <= 3:
            return n - 1

        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2

    def integerBreakRecursive(self, n: int) -> int:
        @functools.cache
        def dp(num):
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))

            return ans

        if n <= 3:
            return n - 1

        return dp(n)

    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        for i in [1, 2, 3]:
            dp[i] = i

        for num in range(4, n + 1):
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp[num - i])

            dp[num] = ans

        return dp[n]


if __name__ == "__main__":
    assert Solution().integerBreak(10) == 36
    assert Solution().integerBreak(2) == 1
