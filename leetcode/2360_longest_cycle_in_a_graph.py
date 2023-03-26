from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        res = -1

        def dfs(node):
            nonlocal visit, dist, res

            visit[node] = True

            neighbor = edges[node]

            if neighbor != -1:
                if not visit[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    dfs(neighbor)
                elif neighbor in dist:
                    res = max(res, dist[node] - dist[neighbor] + 1)

        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                dist = dict()
                dist[i] = 1
                dfs(i)

        return res


if __name__ == "__main__":
    assert Solution().longestCycle(edges=[3, 3, 4, 2, 3]) == 3
    assert Solution().longestCycle(edges=[2, -1, 3, 1]) == -1
