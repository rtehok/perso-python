import collections
from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1


class Solution:
    def isBipartiteBFS(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for node in range(n):
            if color[node] == 0:  # unvisited
                q = collections.deque()
                q.append(node)

                color[node] = 1

                while q:
                    curr = q.popleft()
                    curr_color = color[curr]

                    for neighbor in graph[curr]:
                        if color[neighbor] == curr_color:
                            return False
                        elif color[neighbor] == 0:
                            q.append(neighbor)
                            color[neighbor] = -curr_color

        return True

    def isBipartiteDFS(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        visit = [False] * n

        def dfs(node, curr_color):
            color[node] = curr_color
            visit[node] = True

            for neighbor in graph[node]:
                if visit[neighbor]:
                    if color[neighbor] == curr_color:
                        return False
                else:
                    if not dfs(neighbor, -curr_color):
                        return False
            return True

        for node in range(n):
            if not visit[node]:
                if not dfs(node, 1):
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        dsu = DSU(n)

        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                if dsu.find(node) == dsu.find(neighbor):
                    return False
                dsu.union(neighbors[0], neighbor)
        return True


if __name__ == "__main__":
    assert not Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
