import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        minutes = 0
        fresh = 0

        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while q:
            q_len = len(q)
            for _ in range(q_len):
                x, y = q.popleft()
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes - 1


if __name__ == "__main__":
    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert Solution().orangesRotting([
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]) == -1
    assert Solution().orangesRotting([[0, 2]]) == 0
    assert Solution().orangesRotting([[0]]) == 0
    assert Solution().orangesRotting([[0, 2, 2]]) == 0
    assert Solution().orangesRotting([
        [2, 1, 1],
        [1, 1, 1],
        [0, 1, 2]]) == 2
