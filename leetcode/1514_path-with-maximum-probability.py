import collections
import heapq
from typing import List


class Solution:
    def maxProbabilityV1(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        visit = set()

        def dfs(i, prob):
            if i == end:
                return prob

            max_prob = 0

            visit.add(i)

            for (neighbor, neighbor_prob) in graph[i]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    max_prob = max(max_prob, dfs(neighbor, prob * neighbor_prob))
                    visit.remove(neighbor)

            return max_prob

        return dfs(start, 1)

    # Bellman-Ford Algorithm
    # TC O(m * n) / SC O(n)
    def maxProbabilityBellmanFord(self, n: int, edges: List[List[int]], succProb: List[float], start: int,
                                  end: int) -> float:
        max_prob = [0] * n
        max_prob[start] = 1

        for i in range(n - 1):
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1

            if not has_update:
                break

        return max_prob[end]

    # BFS
    # TC O(m * n) / SC O(n + m)
    def maxProbabilityBFS(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        max_prob = [0] * n
        max_prob[start] = 1

        q = collections.deque([start])
        while q:
            curr = q.popleft()
            for next_node, path_prob in graph[curr]:
                if max_prob[curr] * path_prob > max_prob[next_node]:
                    max_prob[next_node] = max_prob[curr] * path_prob
                    q.append(next_node)

        return max_prob[end]

    # Dijkstra's algo
    # TC O(m + n * log n) / SC O(n + m)
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        max_prob = [0] * n
        max_prob[start] = 1
        q = [(-1, start)]
        while q:
            curr_prob, curr = heapq.heappop(q)
            if curr == end:
                return -curr_prob

            for next_node, path_prob in graph[curr]:
                if -curr_prob * path_prob > max_prob[next_node]:
                    max_prob[next_node] = -curr_prob * path_prob
                    heapq.heappush(q, (-max_prob[next_node], next_node))

        return 0


if __name__ == "__main__":
    assert Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0,
                                     end=2) == 0.25
    assert Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0,
                                     end=2) == 0.3
    assert Solution().maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2) == 0.0
