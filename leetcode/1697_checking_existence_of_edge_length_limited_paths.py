import collections
import math
from typing import List


class Solution:
    def distanceLimitedPathsExistDFS(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = dict()
        for a, b, dis in edgeList:
            if a not in graph:
                graph[a] = dict()
                graph[a][b] = dis
            elif a in graph:
                if b in graph[a]:
                    graph[a][b] = min(graph[a][b], dis)
                else:
                    graph[a][b] = dis

            if b not in graph:
                graph[b] = dict()
                graph[b][a] = dis
            elif b in graph:
                if a in graph[b]:
                    graph[b][a] = min(graph[b][a], dis)
                else:
                    graph[b][a] = dis

        res = []

        def dfs(p, q, limit):
            if p == q:
                res[-1] = True

            visit[p] = True

            for neighbor in graph[p]:
                neighbor_dis = graph[p][neighbor]
                if not visit[neighbor] and neighbor_dis < limit:
                    visit[neighbor] = True
                    dfs(neighbor, q, limit)

        for p, q, limit in queries:
            visit = [False] * n
            res.append(False)
            if p in graph:
                dfs(p, q, limit)

        return res

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        queries_count = len(queries)
        answer = [False] * queries_count

        queries_with_index = [query + [i] for i, query in enumerate(queries)]

        edgeList.sort(key=lambda x: x[2])  # sort by weight
        queries_with_index.sort(key=lambda x: x[2])  # sort by limit
        edges_index = 0

        for p, q, limit, original_index in queries_with_index:
            while edges_index < len(edgeList) and edgeList[edges_index][2] < limit:
                node1 = edgeList[edges_index][0]
                node2 = edgeList[edges_index][1]
                uf.join(node1, node2)
                edges_index += 1

            answer[original_index] = uf.are_connected(p, q)

        return answer


class UnionFind:
    # https://leetcode.com/discuss/general-discussion/1072418/Disjoint-Set-Union-(DSU)Union-Find-A-Complete-Guide
    def __init__(self, size):
        self.parent = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.parent[i] = i

    def find(self, node):  # path-optimized to avoid O(n) search
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def join(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)

        if node1 == node2:
            return

        if self.rank[node1] > self.rank[node2]:  # height optimized
            self.parent[node2] = node1
        else:
            self.parent[node1] = node2
            self.rank[node2] += 1

    def are_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


if __name__ == "__main__":
    assert Solution().distanceLimitedPathsExist(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                                queries=[[0, 1, 2], [0, 2, 5]]) == [False, True]
    assert Solution().distanceLimitedPathsExist(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                                queries=[[0, 4, 14], [1, 4, 13]]) == [True, False]
