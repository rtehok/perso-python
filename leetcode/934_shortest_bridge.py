import collections
import math
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1 or (i, j) in visited:
                return
            visited.add((i, j))

            grid[i][j] = 2

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # find first island and change value to 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            if visited:
                break

        q = collections.deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        flips = 0

        while q:
            q_len = len(q)
            for _ in range(q_len):
                x, y = q.popleft()
                for dx, dy in {(0, 1), (0, -1), (-1, 0), (1, 0)}:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 2 and (nx, ny) not in visited:
                        if grid[nx][ny] == 1:
                            return flips
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        grid[nx][ny] = 2
            flips += 1

        return -1


if __name__ == "__main__":
    assert Solution().shortestBridge(grid=[[0, 1],
                                           [1, 0]]) == 1
    assert Solution().shortestBridge(grid=[[0, 1, 0],
                                           [0, 0, 0],
                                           [0, 0, 1]]) == 2
    assert Solution().shortestBridge(grid=[[1, 1, 1, 1, 1],
                                           [1, 0, 0, 0, 1],
                                           [1, 0, 1, 0, 1],
                                           [1, 0, 0, 0, 1],
                                           [1, 1, 1, 1, 1]]) == 1
