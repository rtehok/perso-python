import collections
from typing import List


class Solution:
    def removeStonesDFS(self, stones: List[List[int]]) -> int:
        visit = set()

        def dfs(r, c):
            visit.add((r, c))
            for x, y in stones:
                if (x, y) not in visit and (x == r or y == c):
                    dfs(x, y)

        count = 0
        n = len(stones)

        for i, j in stones:
            if (i, j) not in visit:
                dfs(i, j)
                count += 1

        return n - count

    def removeStonesBFS(self, stones: List[List[int]]) -> int:
        connected_cols = collections.defaultdict(list)
        connected_rows = collections.defaultdict(list)

        for r, c in stones:
            connected_cols[r].append(c)
            connected_rows[c].append(r)

        count = 0
        visit = set()
        q = collections.deque()

        for a, b in stones:
            if (a, b) not in visit:
                q.append((a, b))

                while q:
                    x, y = q.popleft()

                    if (x, y) in visit:
                        continue

                    visit.add((x, y))

                    count += 1

                    for next_y in connected_cols[x]:
                        if next_y != y:
                            q.append((x, next_y))

                    for next_x in connected_rows[y]:
                        if next_x != x:
                            q.append((next_x, y))

                    connected_cols[x].clear()  # remove because already done
                    connected_rows[y].clear()

                count -= 1  # cannot remove remaining stone

        return count

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = DSU(n)
        col_prev = {}
        row_prev = {}

        for i, (x, y) in enumerate(stones):
            if x in row_prev:
                uf.join(i, row_prev[x])
            if y in col_prev:
                uf.join(i, col_prev[y])

            row_prev[x] = i
            col_prev[y] = i

        return len(stones) - uf.count


class DSU:
    def __init__(self, size):
        self.parent = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.parent[i] = i
        self.count = size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[u] = v
            self.rank[v] += 1
        self.count -= 1


if __name__ == "__main__":
    assert Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
    assert Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
    assert Solution().removeStones([[0, 0]]) == 0
    assert Solution().removeStones([[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]) == 5
