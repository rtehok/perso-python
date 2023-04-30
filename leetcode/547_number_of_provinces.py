import collections
from typing import List


class Solution:
    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(node):
            visit[node] = True
            for j in range(n):
                if isConnected[node][j] and not visit[j]:
                    dfs(j)

        count = 0
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                dfs(i)
                count += 1

        return count

    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def bfs(node):
            q = collections.deque()
            q.append(node)
            visit[node] = True

            while q:
                next_node = q.popleft()
                for j in range(n):
                    if isConnected[next_node][j] and not visit[j]:
                        visit[j] = True
                        q.append(j)

        count = 0
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                bfs(i)
                count += 1

        return count

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = DSU(n)

        count = n

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    uf.join(i, j)
                    count -= 1

        return count


class DSU:
    def __init__(self, size):
        self.parent = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.parent[i] = i

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


if __name__ == "__main__":
    assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert Solution().findCircleNum([[1, 0, 0, 1],
                                     [0, 1, 1, 0],
                                     [0, 1, 1, 1],
                                     [1, 0, 1, 1]]) == 1
