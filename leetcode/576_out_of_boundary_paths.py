class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """ Brute Force """
        # if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
        #     return 1
        # if maxMove == 0:
        #     return 0
        #
        # return self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) + \
        #        self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn) + \
        #        self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) + \
        #        self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)

        """ Brute Force + memoization"""
        # M = int(1e9 + 7)
        # memo = {}
        #
        # def helper(i, j, k):
        #     if i == m or j == n or i < 0 or j < 0:
        #         return 1
        #     if k == 0:
        #         return 0
        #
        #     if (i, j, k) in memo:
        #         return memo[(i, j, k)]
        #
        #     memo[(i, j, k)] = ((helper(i - 1, j, k - 1) + helper(i + 1, j, k - 1)) % M + \
        #                        (helper(i, j + 1, k - 1) + helper(i, j - 1, k - 1)) % M) % M
        #
        #     # (a + b) % M == (a % m + b % m) % m
        #
        #     return memo[(i, j, k)]
        #
        # return helper(startRow, startColumn, maxMove)

        """ DP tabulation """
        M = int(1e9 + 7)
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        count = 0

        for _ in range(maxMove):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + dp[i][j]) % M
                    if j == n - 1:
                        count = (count + dp[i][j]) % M
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M
                    tmp[i][j] = (((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % M + (
                                (dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % M) % M
            dp = tmp

        return count


if __name__ == "__main__":
    # assert Solution().findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
    assert Solution().findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
    assert Solution().findPaths(2, 3, 8, 1, 0) == 1104
