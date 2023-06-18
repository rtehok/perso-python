from typing import List


class Solution:
    # TC O(m * n * log(m * n)) / SC O(m * n)
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = {(-1, 0), (1, 0), (0, -1), (0, 1)}

        MOD = 10 ** 9 + 7

        dp = [[1] * n for _ in range(m)]  # represents the number of paths that end at each cell

        index_list = [[i, j] for i in range(m) for j in range(n)]
        index_list.sort(key=lambda x: grid[x[0]][x[1]])

        for i, j in index_list:
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    dp[ni][nj] += dp[i][j]
                    dp[ni][nj] %= MOD

        return sum(sum(row) for row in dp) % MOD

    # TC O(m * n) / SC O(m * n)
    def countPathsDFS(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = {(-1, 0), (1, 0), (0, -1), (0, 1)}

        dp = [[0] * n for _ in range(m)]

        MOD = 10 ** 9 + 7

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            ans = 1  # path is grid[i][j] itself

            for dx, dy in moves:
                prev_x = i + dx
                prev_y = j + dy
                # check if smaller and traverse
                if 0 <= prev_x < m and 0 <= prev_y < n and grid[prev_x][prev_y] < grid[i][j]:
                    ans += dfs(prev_x, prev_y) % MOD

            dp[i][j] = ans
            return ans

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % MOD


if __name__ == "__main__":
    assert Solution().countPaths([[1, 1], [3, 4]]) == 8
    assert Solution().countPaths([[1], [2]]) == 3
