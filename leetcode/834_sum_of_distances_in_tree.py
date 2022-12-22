import collections
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * n
        count = [1] * n

        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs(0, None)
        dfs2(0, None)
        return res


if __name__ == "__main__":
    assert Solution().sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == \
           [8, 12, 6, 10, 10, 10]
    assert Solution().sumOfDistancesInTree(n=2, edges=[[1, 0]]) == [1, 1]
    assert Solution().sumOfDistancesInTree(n=1, edges=[]) == [0]
