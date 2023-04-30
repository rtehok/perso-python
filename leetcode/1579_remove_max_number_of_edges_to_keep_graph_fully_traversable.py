from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_bob = DSU(n)
        uf_alice = DSU(n)

        edges_required = 0

        # first build for type 3
        for t, a, b in edges:
            if t == 3:
                edges_required += uf_alice.join(a, b) | uf_bob.join(a, b)  # join returns 0 or 1

        for t, a, b in edges:
            if t == 1:
                edges_required += uf_alice.join(a, b)
            elif t == 2:
                edges_required += uf_bob.join(a, b)

        if uf_alice.is_connected() and uf_bob.is_connected():
            return len(edges) - edges_required

        return -1


class DSU:
    def __init__(self, size):
        self.parent = [0] * (size + 1)  # indexes are 1 to n
        for i in range(size + 1):
            self.parent[i] = i
        self.rank = [0] * (size + 1)
        self.count = size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return 0

        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[u] = v
            self.rank[v] += 1

        self.count -= 1

        return 1

    def is_connected(self):
        return self.count == 1


if __name__ == "__main__":
    assert Solution().maxNumEdgesToRemove(n=4,
                                          edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]) == 2
    assert Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]) == 0
    assert Solution().maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]) == -1
