import collections
from typing import List


class Solution:
    def closedIslandV1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        visit = [[False] * n for _ in range(m)]

        def next_moves(i, j):
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = i + x
                c = j + y
                yield r, c

        nb_island = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if grid[i][j] == 1 or visit[i][j]:
                return True

            visit[i][j] = True
            is_closed = True

            for next_x, next_y in next_moves(i, j):
                if not dfs(next_x, next_y):
                    is_closed = False

            return is_closed

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and dfs(i, j):
                    nb_island += 1

        return nb_island

    def closedIslandDFS(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if grid[i][j] == 1:
                return True

            grid[i][j] = 1  # mark as visited

            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i + 1, j)
            down = dfs(i - 1, j)

            return left and right and up and down

        nb_island = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    nb_island += 1

        return nb_island

    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))

            visit[i][j] = True
            is_closed = True

            while q:
                x, y = q.popleft()

                for next_x, next_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r = x + next_x
                    c = y + next_y
                    if r < 0 or c < 0 or r >= m or c >= n:
                        is_closed = False
                    elif not visit[r][c] and grid[r][c] == 0:
                        visit[r][c] = True
                        q.append((r, c))

            return is_closed

        nb_island = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and bfs(i, j):
                    nb_island += 1

        return nb_island


if __name__ == "__main__":
    assert Solution().closedIsland(
        grid=[[1, 1, 1, 1, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0]]) == 2
    assert Solution().closedIsland(
        grid=[[0, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 1, 1, 1, 0]]) == 1
    assert Solution().closedIsland(
        grid=[[1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1]]) == 2
    assert Solution().closedIsland(
        [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    ) == 5
