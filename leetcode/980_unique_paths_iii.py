from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = 0

        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        m, n = len(grid), len(grid[0])
        start_x = 0
        start_y = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    start_x = row
                    start_y = col

        zeros = sum(row.count(0) for row in grid)  # count number of zeros to walk over

        def dfs(i, j, zeros):
            nonlocal res

            grid[i][j] = 3  # change to track walk over

            for r, c in moves:
                x = i + r
                y = j + c
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0:
                        dfs(x, y, zeros - 1)
                    if grid[x][y] == 2 and zeros == 0:
                        res += 1

            grid[i][j] = 0  # put back after finished (back track)

            return

        dfs(start_x, start_y, zeros)

        return res


if __name__ == "__main__":
    assert Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
    assert Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
    assert Solution().uniquePathsIII([[0, 1], [2, 0]]) == 0
