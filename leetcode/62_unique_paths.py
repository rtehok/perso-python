class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # moves = [(1, 0), (0, 1)]
        #
        # q = deque()
        # q.append((0, 0))
        #
        # def getPossibleMove(i, j):
        #     for move in moves:
        #         x = i + move[0]
        #         y = j + move[1]
        #         if x <= m - 1 and y <= n - 1:
        #             yield x, y
        #
        # res = 0
        # while q:
        #     i, j = q.popleft()
        #
        #     if i == m - 1 and j == n - 1:
        #         res += 1
        #
        #     possible_moves = getPossibleMove(i, j)
        #
        #     for possible_move in possible_moves:
        #         q.append((possible_move[0], possible_move[1]))
        #
        # return res

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0] = [1 for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(3, 7))
