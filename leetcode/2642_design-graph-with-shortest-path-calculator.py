import heapq
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for from_i, to_i, cost_i in edges:
            self.graph[from_i].append((to_i, cost_i))

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.graph)
        pq = [(0, node1)]
        cost_for_node = [float("inf")] * n
        cost_for_node[node1] = 0

        while pq:
            curr_cost, node = heapq.heappop(pq)
            if node == node2:
                return curr_cost

            for neighbor, cost in self.graph[node]:
                new_cost = curr_cost + cost
                if new_cost < cost_for_node[neighbor]:
                    cost_for_node[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))

        return -1


if __name__ == "__main__":
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    assert g.shortestPath(3, 2) == 6
    assert g.shortestPath(0, 3) == -1
    g.addEdge([1, 3, 4])
    assert g.shortestPath(0, 3) == 6
