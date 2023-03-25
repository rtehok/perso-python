import collections
from typing import List


class Solution:
    def countPairsDFS(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node):
            nonlocal visit

            count = 1
            visit[node] = True

            for neighbor in graph[node]:
                if not visit[neighbor]:
                    count += dfs(neighbor)

            return count

        res = 0
        remaining_nodes = n
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                size_components = dfs(i)

                res += size_components * (remaining_nodes - size_components)

                remaining_nodes -= size_components

        return res

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def bfs(node):
            nonlocal visit

            count = 1

            visit[node] = True
            q = collections.deque()
            q.append(node)

            while q:
                nde = q.popleft()

                for neighbor in graph[nde]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        q.append(neighbor)
                        count += 1

            return count

        res = 0
        remaining_nodes = n
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                size_components = bfs(i)

                res += size_components * (remaining_nodes - size_components)

                remaining_nodes -= size_components

        return res


if __name__ == "__main__":
    assert Solution().countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14
    assert Solution().countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]]) == 0
