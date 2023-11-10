import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None

        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        ans = []

        def dfs(node, prev):
            ans.append(node)
            for next_node in graph[node]:
                if next_node != prev:
                    dfs(next_node, node)

        dfs(root, None)

        return ans


if __name__ == "__main__":
    assert Solution().restoreArray([[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4]
    assert Solution().restoreArray([[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3]
    assert Solution().restoreArray([[100000, -100000]]) == [100000, -100000]
