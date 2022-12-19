from collections import defaultdict
from typing import List


class Solution:
    def validPathDFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(node):
            if node == destination:
                return True

            if not seen[node]:
                seen[node] = True
                for next_node in graph[node]:
                    if dfs(next_node):
                        return True

            return False

        return dfs(source)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n
        seen[source] = True
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for next_node in graph[node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)

        return False


if __name__ == "__main__":
    assert Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert not Solution().validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5)
    assert Solution().validPath(n=1, edges=[], source=0, destination=0)
