class Solution:
    def findPathsV1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        MOD = 10 ** 9 + 7

        def dfs(i, j, remaining_moves):
            if remaining_moves < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            if (i, j, remaining_moves) in memo:
                return memo[(i, j, remaining_moves)]

            memo[(i, j, remaining_moves)] = (dfs(i + 1, j, remaining_moves - 1) +
                                             dfs(i - 1, j, remaining_moves - 1) +
                                             dfs(i, j + 1, remaining_moves - 1) +
                                             dfs(i, j - 1, remaining_moves - 1)) % MOD
            return memo[(i, j, remaining_moves)]

        return dfs(startRow, startColumn, maxMove)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        cnt = 0

        for _ in range(maxMove):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        cnt += dp[i][j]
                        cnt %= MOD
                    if j == n - 1:
                        cnt += dp[i][j]
                        cnt %= MOD
                    if i == 0:
                        cnt += dp[i][j]
                        cnt %= MOD
                    if j == 0:
                        cnt += dp[i][j]
                        cnt %= MOD

                    tmp[i][j] = ((dp[i - 1][j] if i > 0 else 0) +
                                 (dp[i + 1][j] if i < m - 1 else 0) +
                                 (dp[i][j - 1] if j > 0 else 0) +
                                 (dp[i][j + 1] if j < n - 1 else 0)
                                 ) % MOD

            dp = tmp
        return cnt


if __name__ == "__main__":
    assert Solution().findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
    assert Solution().findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
    assert Solution().findPaths(2, 3, 8, 1, 0) == 1104
