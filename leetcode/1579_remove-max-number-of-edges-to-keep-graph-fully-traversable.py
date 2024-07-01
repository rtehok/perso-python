from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)

        edges_required = 0

        for edge_type, x, y in edges:
            if edge_type == 3:
                edges_required += (alice.union(x, y) | bob.union(x, y))

        for edge_type, x, y in edges:
            if edge_type == 2:
                edges_required += bob.union(x, y)
            elif edge_type == 1:
                edges_required += alice.union(x, y)

        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required

        return -1


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
        self.components = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return 0
        else:
            if self.rank[u] < self.rank[v]:
                u, v = v, u

            self.parent[v] = u
            self.rank[u] += self.rank[v]

            self.components -= 1

            return 1

    def is_connected(self):
        return self.components == 1


assert Solution().maxNumEdgesToRemove(n=4,
                                      edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]) == 2
assert Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]) == 0
assert Solution().maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]) == -1
