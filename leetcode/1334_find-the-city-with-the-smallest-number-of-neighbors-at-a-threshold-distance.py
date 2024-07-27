import heapq
from collections import defaultdict
from typing import List


class Solution:
    def get_city_with_fewest_reachable(self, n: int, shortest_path_matrix: List[List[int]], distanceThreshold: int):
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if i != j and shortest_path_matrix[i][j] <= distanceThreshold)
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i

        return city_with_fewest_reachable

    def findTheCityDijkstra(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(set)
        for u, v, w in edges:
            graph[u].add((v, w))
            graph[v].add((u, w))

        def dijkstra(start):
            shortest_path_distance = [float("inf")] * n
            shortest_path_distance[start] = 0

            pq = [(0, start)]
            while pq:
                curr_dist, curr_city = heapq.heappop(pq)

                if curr_dist > shortest_path_distance[curr_city]:
                    continue

                for neighbor_city, edge_weight in graph[curr_city]:
                    if (shortest_path_distance[neighbor_city] > curr_dist + edge_weight):
                        shortest_path_distance[neighbor_city] = curr_dist + edge_weight
                        heapq.heappush(pq, (curr_dist + edge_weight, neighbor_city))

            return shortest_path_distance

        shortest_path_matrix = [dijkstra(i) for i in range(n)]

        return self.get_city_with_fewest_reachable(n, shortest_path_matrix, distanceThreshold)

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance_matrix = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            distance_matrix[i][i] = 0

        for start, end, weight in edges:
            distance_matrix[start][end] = weight
            distance_matrix[end][start] = weight

        def floyd():
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        distance_matrix[i][j] = min(
                            distance_matrix[i][j],
                            distance_matrix[i][k] + distance_matrix[k][j]
                        )

        floyd()

        return self.get_city_with_fewest_reachable(n, distance_matrix, distanceThreshold)


assert Solution().findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4) == 3
assert Solution().findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
                              distanceThreshold=2) == 0
