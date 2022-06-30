from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        time = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in moves:
                    if 0 <= r + dr <= m - 1 and 0 <= c + dc <= n - 1 and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))

            time += 1

        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1

        return time - 1 if time > 0 else time


if __name__ == "__main__":
    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert Solution().orangesRotting([[2, 1, 1],
                                      [0, 1, 1],
                                      [1, 0, 1]]) == -1
    assert Solution().orangesRotting([[0, 2]]) == 0
