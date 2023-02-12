import collections
import math
from typing import List


class Solution:
    def minimumFuelCostBFS(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1

        degree = [0] * n

        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
            degree[a] += 1
            degree[b] += 1

        q = collections.deque([])
        for i in range(1, n):
            if degree[i] == 1:
                q.append(i)

        fuel = 0
        representatives = [1] * n

        while q:
            node = q.popleft()
            fuel += math.ceil(representatives[node] / seats)
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                representatives[neighbor] += representatives[node]
                if degree[neighbor] == 1 and neighbor != 0:
                    q.append(neighbor)

        return fuel

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        visited = set()

        def dfs(node):
            nonlocal visited
            visited.add(node)
            cost_fuel = 0
            num_rep = 1

            for neighbor in graph[node]:
                if neighbor not in visited:
                    node_fuel, nb_child_rep = dfs(neighbor)
                    num_rep += nb_child_rep
                    cost_fuel += node_fuel + math.ceil(nb_child_rep / seats)
            return cost_fuel, num_rep

        fuel, _ = dfs(0)
        return fuel


if __name__ == "__main__":
    assert Solution().minimumFuelCost(roads=[[0, 1], [0, 2], [0, 3]], seats=5) == 3
    assert Solution().minimumFuelCost(roads=[], seats=1) == 0
    assert Solution().minimumFuelCost([[0, 1], [0, 2], [3, 2], [0, 4], [1, 5], [5, 6], [3, 7]], 1) == 13
    assert Solution().minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2) == 7
