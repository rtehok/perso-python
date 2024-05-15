from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)

        q = deque()
        # Mark thieves as 0 and empty cells as -1, and push thieves to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        # Calculate safeness factor for each cell using BFS
        while q:
            q_len = len(q)
            while q_len:
                i, j = q.popleft()
                for dx, dy in dir:
                    nx, ny = dx + i, dy + j
                    val = grid[i][j]

                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == -1:
                        # update safeness factor
                        grid[nx][ny] = val + 1
                        q.append((nx, ny))
                q_len -= 1

        start, end, res = 0, 0, -1
        for i in range(n):
            for j in range(n):
                end = max(end, grid[i][j])

        def isValidSafeness(min_safeness):
            if grid[0][0] < min_safeness or grid[-1][-1] < min_safeness:
                return False

            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while q:
                i, j = q.popleft()
                if i == n - 1 and j == n - 1:
                    return True

                for dx, dy in dir:
                    nx, ny = dx + i, dy + j
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] >= min_safeness:
                        visited[nx][ny] = True
                        q.append((nx, ny))

            return False

        while start <= end:
            mid = start + (end - start) // 2
            if isValidSafeness(mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1

        return res


# assert Solution().maximumSafenessFactor(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
assert Solution().maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2
assert Solution().maximumSafenessFactor(grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]) == 2
