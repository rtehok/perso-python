import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrixDFS(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        def dfs(i, j, length):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] == 1:
                return

            if i == j == n - 1:
                nonlocal min_length
                min_length = min(min_length, length)
                return

            grid[i][j] = 1  # mark as visited

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = i + dx, j + dy
                    dfs(nx, ny, length + 1)

            grid[i][j] = 0  # backtrack: mark cell as unvisited

        min_length = float("inf")
        dfs(0, 0, 1)
        return -1 if min_length == float("inf") else min_length

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visit = set()

        q = collections.deque()
        q.append((0, 0))
        path = 1

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                if i == j == n - 1:
                    return path

                for di, dj in moves:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in visit:
                        visit.add((ni, nj))
                        q.append((ni, nj))
            path += 1

        return -1


if __name__ == "__main__":
    assert Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    assert Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
