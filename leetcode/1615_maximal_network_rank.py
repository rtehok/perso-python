import collections
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        max_rank = 0

        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                current_rank = len(graph[node1]) + len(graph[node2])
                if node2 in graph[node1]:
                    current_rank -= 1

                max_rank = max(max_rank, current_rank)

        return max_rank


if __name__ == "__main__":
    assert Solution().maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]) == 4
    assert Solution().maximalNetworkRank(n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]) == 5
    assert Solution().maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]) == 5
