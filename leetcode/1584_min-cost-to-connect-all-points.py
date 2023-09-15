from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)

        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()

        dsu = DSU(n)

        edges_added = 0
        for dist, i, j in edges:
            if dsu.find(i) != dsu.find(j):
                dsu.join(i, j)
                res += dist
                edges_added += 1
                if edges_added == n - 1:
                    break

        return res

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            if self.rank[u] < self.rank[v]:
                u, v = v, u

            self.parent[v] = u
            self.rank[u] += self.rank[v]


if __name__ == "__main__":
    assert Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
