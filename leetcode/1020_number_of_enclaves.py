import collections
from typing import List


class Solution:
    def numEnclavesBFS(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        def bfs(i, j):
            nonlocal res

            visit[i][j] = True
            cnt = 1
            is_enclosed = True

            q = collections.deque()
            q.append((i, j))

            while q:
                q_i, q_j = q.popleft()
                for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    r = q_i + x
                    c = q_j + y
                    if r < 0 or c < 0 or r >= m or c >= n:
                        is_enclosed = False
                        cnt = 0
                    elif grid[r][c] == 1 and not visit[r][c]:
                        visit[r][c] = True
                        if is_enclosed:
                            cnt += 1
                        else:
                            cnt = 0
                        q.append((r, c))

            return cnt

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visit[i][j]:
                    res += bfs(i, j)

        return res

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            if grid[i][j] == 0:
                return

            grid[i][j] = 0

            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        # first / last column
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][-1] == 1:
                dfs(i, n - 1)

        # first / last row
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[-1][j] == 1:
                dfs(m - 1, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1:
                    res += 1

        return res


if __name__ == "__main__":
    assert Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == 0
    assert Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3
    assert Solution().numEnclaves(
        [[0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
         [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
         [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]) == 3
