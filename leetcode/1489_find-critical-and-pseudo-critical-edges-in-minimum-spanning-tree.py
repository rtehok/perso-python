from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = [edge.copy() for edge in edges]

        for i, edge in enumerate(new_edges):
            edge.append(i)

        new_edges.sort(key=lambda x: x[2])  # sort by weight

        uf_std = DSU(n)
        std_weight = 0  # min_weight
        for u, v, w, _ in new_edges:
            # only connect new nodes
            if uf_std.join(u, v):
                std_weight += w

        critical = []
        pseudo_critical = []

        for u, v, w, i in new_edges:
            uf_ignore = DSU(n)
            ignore_weight = 0

            for x, y, w_ignore, j in new_edges:
                if i != j and uf_ignore.join(x, y):
                    ignore_weight += w_ignore

            # if disconnected or total weight is greater, the i-th edge is critical
            if uf_ignore.max_size < n or ignore_weight > std_weight:
                critical.append(i)
                # count only once
                continue

            uf_force = DSU(n)
            force_weight = w
            uf_force.join(u, v)

            for x, y, w_force, j in new_edges:
                if i != j and uf_force.join(x, y):
                    force_weight += w_force

            # if same weight, the edge is pseudo-critical
            if force_weight == std_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.max_size = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, u, v) -> bool:
        u, v = self.find(u), self.find(v)

        if u == v:
            return False

        if self.rank[u] > self.rank[v]:
            u, v = v, u

        self.parent[u] = v
        self.rank[v] += self.rank[u]
        self.max_size = max(self.max_size, self.rank[v])
        return True


if __name__ == "__main__":
    assert Solution().findCriticalAndPseudoCriticalEdges(n=5,
                                                         edges=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3],
                                                                [3, 4, 3], [1, 4, 6]]) == [[0, 1], [2, 3, 4, 5]]
    assert Solution().findCriticalAndPseudoCriticalEdges(n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]) == [
        [], [0, 1, 2, 3]]
