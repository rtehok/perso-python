import collections
import math
from typing import List


class Solution:
    # TC O(n2)
    # SC O(n2)
    def maxDistanceBFS(self, grid: List[List[int]]) -> int:
        distance = -1

        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        n = len(grid)

        visited = [[None] * n for _ in range(n)]

        q = collections.deque([])

        for i in range(n):
            for j in range(n):
                visited[i][j] = grid[i][j]
                if grid[i][j] == 1:
                    q.append((i, j))

        while q:
            q_size = len(q)

            while q_size > 0:

                r, c = q.popleft()

                for x, y in moves:
                    row = r + x
                    col = c + y
                    if (0 <= row <= n - 1) and (0 <= col <= n - 1) and (visited[row][col] == 0):
                        visited[row][col] = 1
                        q.append((row, col))

                q_size -= 1

            distance += 1

        return -1 if distance == 0 else distance

    # TC O(n2)
    # SC O(n2)
    def maxDistanceDP(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_distance = 2 * n + 1

        dist = [[max_distance] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                else:
                    dist[i][j] = min(dist[i][j],
                                     dist[i - 1][j] + 1 if i > 0 else max_distance,
                                     dist[i][j - 1] + 1 if j > 0 else max_distance)

        distance = -math.inf
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dist[i][j] = min(dist[i][j],
                                 dist[i + 1][j] + 1 if i < n - 1 else max_distance,
                                 dist[i][j + 1] + 1 if j < n - 1 else max_distance)
                distance = max(distance, dist[i][j])

        return -1 if distance == 0 or distance == max_distance else distance

    # TC O(n2)
    # SC O(1) but need to modify grid
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_distance = 2 * n + 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = max_distance
                    grid[i][j] = min(grid[i][j],
                                     grid[i - 1][j] + 1 if i > 0 else max_distance,
                                     grid[i][j - 1] + 1 if j > 0 else max_distance)

        distance = -math.inf
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                grid[i][j] = min(grid[i][j],
                                 grid[i + 1][j] + 1 if i < n - 1 else max_distance,
                                 grid[i][j + 1] + 1 if j < n - 1 else max_distance)
                distance = max(distance, grid[i][j])

        return -1 if distance == 0 or distance == max_distance else distance


if __name__ == "__main__":
    assert Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
    assert Solution().maxDistance(
        [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == -1
    assert Solution().maxDistance([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == -1
