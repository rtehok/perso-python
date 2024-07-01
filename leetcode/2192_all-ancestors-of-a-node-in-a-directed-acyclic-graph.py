import collections
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            neighbors[a].append(b)
            degree[b] += 1

        q = collections.deque([i for i in range(n) if degree[i] == 0])

        topological_sort = []
        while q:
            curr = q.popleft()
            topological_sort.append(curr)

            for neighbor in neighbors[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    q.append(neighbor)

        ancestors = [[] for _ in range(n)]
        ancestors_set = [set() for _ in range(n)]

        for node in topological_sort:
            for neighbor in neighbors[node]:
                ancestors_set[neighbor].add(node)
                ancestors_set[neighbor].update(ancestors_set[node])

        for i in range(n):
            ancestors[i].extend((ancestors_set[i]))
            ancestors[i].sort()

        return ancestors


assert Solution().getAncestors(n=8,
                               edges=[[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]) == [
           [], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
assert Solution().getAncestors(n=5, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4],
                                           [3, 4]]) == [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
