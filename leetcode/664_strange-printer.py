class Solution:
    def strangePrinterBottomUp(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i + 1][right])

                if j == -1:
                    dp[left][right] = 0

        return dp[0][n - 1] + 1

    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(left, right):
            if dp[left][right] != -1:
                return dp[left][right]

            dp[left][right] = n

            j = -1

            for i in range(left, right):
                if s[i] != s[right] and j == -1:
                    j = i
                if j != -1:
                    dp[left][right] = min(dp[left][right], 1 + solve(j, i) + solve(i + 1, right))

            if j == -1:
                dp[left][right] = 0

            return dp[left][right]

        return solve(0, n - 1) + 1


if __name__ == "__main__":
    assert Solution().strangePrinter("aaabbb") == 2
    assert Solution().strangePrinter("aba") == 2
