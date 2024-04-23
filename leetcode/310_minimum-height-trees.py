from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)

        indegree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        q = deque([i for i in range(n) if indegree[i] == 1])

        processed = 0

        while n - processed > 2:
            size = len(q)
            processed += size
            for _ in range(size):
                curr = q.popleft()
                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        q.append(neighbor)

        return list(q)


assert Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]
assert Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [3, 4]
