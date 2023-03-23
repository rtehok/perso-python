import collections
from typing import List


class Solution:
    def makeConnectedDFS(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = collections.defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        nb_connected = 0
        visit = [False] * n

        def dfs(node):
            visit[node] = True

            if node not in graph:
                return

            for neighbor in graph[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)

        for i in range(n):
            if not visit[i]:
                nb_connected += 1
                dfs(i)

        return nb_connected - 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = collections.defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        nb_connected = 0
        visit = [False] * n

        def bfs(node):
            q = collections.deque()
            q.append(node)

            while q:
                node = q.popleft()
                if node not in graph:
                    continue

                for neighbor in graph[node]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        q.append(neighbor)

        for i in range(n):
            if not visit[i]:
                nb_connected += 1
                bfs(i)

        return nb_connected - 1


if __name__ == "__main__":
    assert Solution().makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]) == 1
    assert Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2
    assert Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]) == -1
    assert Solution().makeConnected(n=15, connections=[[5, 7], [7, 9], [1, 3], [1, 4], [0, 8], [2, 11], [5, 9], [4, 14],
                                                       [7, 8], [3, 10], [9, 12], [5, 11], [4, 7], [2, 4], [2, 5],
                                                       [6, 9], [5, 10]]) == 1
