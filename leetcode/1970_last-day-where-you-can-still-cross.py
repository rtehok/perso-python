import collections
from typing import List


class Solution:
    def latestDayToCrossBFS(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day):
            grid = [[0] * col for _ in range(row)]  # 0 = land
            q = collections.deque()

            for r, c in cells[:day]:
                grid[r - 1][c - 1] = 1  # 1 = water

            for c in range(col):
                if not grid[0][c]:
                    q.append((0, c))  # start from top
                    grid[0][c] = -1  # visit

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True

                for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = -1  # visit
                        q.append((nr, nc))

            return False

        left, right = 1, row * col
        while left < right:
            mid = right - (right - left) // 2

            if canCross(mid):
                left = mid
            else:
                right = mid - 1

        return left

    def latestDayToCrossDFS(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day):
            grid = [[0] * col for _ in range(row)]  # 0 = land

            for r, c in cells[:day]:
                grid[r - 1][c - 1] = 1

            def dfs(r, c):
                if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != 0:
                    return False

                if r == row - 1:
                    return True

                grid[r][c] = -1  # visit

                for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                    if dfs(r + dr, c + dc):
                        return True

                return False

            for c in range(col):
                if grid[0][c] == 0 and dfs(0, c):
                    return True

            return False

        left, right = 1, row * col
        while left < right:
            mid = right - (right - left) // 2

            if canCross(mid):
                left = mid
            else:
                right = mid - 1

        return left

    def latestDayToCrossDSULand(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + 2)
        grid = [[1] * col for _ in range(row)]  # all water

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 0  # replace water by land
            index_1 = r * col + c + 1
            for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                nr, nc = r + dr, c + dc
                index_2 = nr * col + nc + 1
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    dsu.union(index_1, index_2)

            if r == 0:
                dsu.union(0, index_1)

            if r == row - 1:
                dsu.union(row * col + 1, index_1)

            if dsu.find(0) == dsu.find(row * col + 1):
                return i

    # use DSU to connect water from left to right
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + 2)
        grid = [[0] * col for _ in range(row)]  # all land

        for i in range(row * col):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1  # replace land by water
            index_1 = r * col + c + 1
            for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}:  # 8 directions
                nr, nc = r + dr, c + dc
                index_2 = nr * col + nc + 1
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    dsu.union(index_1, index_2)

            # check that you can connect from left to right (with diagonal)
            if c == 0:
                dsu.union(0, index_1)

            if c == col - 1:
                dsu.union(row * col + 1, index_1)

            if dsu.find(0) == dsu.find(row * col + 1):
                return i


class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            u, v = v, u
        self.parents[u] = v
        self.rank[v] += self.rank[u]


if __name__ == "__main__":
    assert Solution().latestDayToCross(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]) == 2
    assert Solution().latestDayToCross(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]) == 1
    assert Solution().latestDayToCross(row=3, col=3,
                                       cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2],
                                              [3, 1]]) == 3
