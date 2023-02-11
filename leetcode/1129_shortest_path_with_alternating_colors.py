import collections
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in redEdges:
            if b != 0:
                graph[a].append((b, 0))
        for a, b in blueEdges:
            if b != 0:
                graph[a].append((b, 1))

        res = [-1] * n
        res[0] = 0

        q = collections.deque([(0, 0, -1)])

        visited = [[False] * 2 for _ in range(n)]
        visited[0][0] = True
        visited[0][1] = True

        while q:
            node, steps, previous_color = q.popleft()
            if node not in graph:
                continue

            for neighbor, color in graph[node]:
                if not visited[neighbor][color] and color != previous_color:
                    if res[neighbor] == -1:
                        res[neighbor] = 1 + steps
                    visited[neighbor][color] = True
                    q.append((neighbor, steps + 1, color))

        return res


if __name__ == "__main__":
    assert Solution().shortestAlternatingPaths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]) == [0, 1, -1]
    assert Solution().shortestAlternatingPaths(n=3, redEdges=[[0, 1]], blueEdges=[[2, 1]]) == [0, 1, -1]
    assert Solution().shortestAlternatingPaths(n=3, redEdges=[[0, 1], [0, 2]], blueEdges=[[1, 0]]) == [0, 1, 1]
    assert Solution().shortestAlternatingPaths(n=5, redEdges=[[2, 0], [4, 3], [4, 4], [3, 0], [1, 4]],
                                               blueEdges=[[2, 1], [4, 3], [3, 1], [3, 0], [1, 1], [2, 0], [0, 3],
                                                          [3, 3], [2, 3]]) == [0, -1, -1, 1, -1]
    assert Solution().shortestAlternatingPaths(n=5,
                                               redEdges=[[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [2, 1], [2, 0], [1, 4],
                                                         [3, 4]],
                                               blueEdges=[[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]) == [0, 1, 2, 1, 1]
