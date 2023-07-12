import collections
from typing import List


class Solution:
    def eventualSafeNodesBFS(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        outdegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for x in graph[i]:
                adj[x].append(i)
                outdegree[i] += 1

        q = collections.deque()
        for i in range(n):
            if outdegree[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # delete edge node -> neighbor
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    q.append(neighbor)

        safe_node = []
        for i in range(n):
            if safe[i]:
                safe_node.append(i)

        return safe_node

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        visit = [False] * n
        inStack = [False] * n

        def dfs(node):
            # if node in stack, there is a cycle
            if inStack[node]:
                return True

            if visit[node]:
                return False

            visit[node] = True

            inStack[node] = True

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            inStack[node] = False

            return False

        for i in range(n):
            dfs(i)

        safe_nodes = []

        for i in range(n):
            if not inStack[i]:
                safe_nodes.append(i)

        return safe_nodes


if __name__ == "__main__":
    assert Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
    assert Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4]
    assert Solution().eventualSafeNodes([[0], [2, 3, 4], [3, 4], [0, 4], []]) == [4]
