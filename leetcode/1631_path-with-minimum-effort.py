import collections
import heapq
from typing import List


class Solution:
    # TLE
    def minimumEffortPathBinarySearch(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        max_effort = max(max(row) for row in heights)

        left, right = 0, max_effort

        while left <= right:
            mid = (left + right) // 2
            visited = [[False] * n for _ in range(m)]

            q = collections.deque([(0, 0)])
            while q:
                x, y = q.popleft()
                visited[x][y] = True

                for dx, dy in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if abs(heights[nx][ny] - heights[x][y]) <= mid:
                            q.append((nx, ny))

            if visited[-1][-1]:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        efforts = [[float("inf")] * n for _ in range(m)]
        efforts[0][0] = 0

        pq = [(0, 0, 0)]  # priority queue (effort, x, y)
        while pq:
            effort, x, y = heapq.heappop(pq)

            if x == m - 1 and y == n - 1:
                return effort

            for dx, dy in directions:
                nx, ny = dx + x, dy + y

                if 0 <= nx < m and 0 <= ny < n:
                    new_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))

                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(pq, (new_effort, nx, ny))

        return -1


if __name__ == "__main__":
    assert Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert Solution().minimumEffortPath(
        [[1, 2, 1, 1, 1],
         [1, 2, 1, 2, 1],
         [1, 2, 1, 2, 1],
         [1, 2, 1, 2, 1],
         [1, 1, 1, 2, 1]]) == 0
