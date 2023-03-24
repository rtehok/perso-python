import collections
from typing import List


class Solution:
    def minReorderDFS(self, n: int, connections: List[List[int]]) -> int:
        res = 0

        graph = collections.defaultdict(set)
        for a, b in connections:
            graph[a].add((b, 1))  # original
            graph[b].add((a, 0))  # artificial

        def dfs(node, parent):
            nonlocal res
            if node not in graph:
                return

            for child, is_original in graph[node]:
                if child != parent:
                    res += is_original
                    dfs(child, node)

        dfs(0, -1)

        return res

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0

        graph = collections.defaultdict(set)
        for a, b in connections:
            graph[a].add((b, 1))  # original
            graph[b].add((a, 0))  # artificial

        q = collections.deque()
        q.append(0)
        visit = [False] * n
        visit[0] = True

        while q:
            node = q.popleft()

            for child, is_original in graph[node]:
                if not visit[child]:
                    visit[child] = True
                    res += is_original
                    q.append(child)

        return res


if __name__ == "__main__":
    assert Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert Solution().minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert Solution().minReorder(n=3, connections=[[1, 0], [2, 0]]) == 0
