from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        res = 0

        def dfs(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '#'
            for move in moves:
                x = i + move[0]
                y = j + move[1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res


if __name__ == "__main__":
    assert Solution().numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1
    assert Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
