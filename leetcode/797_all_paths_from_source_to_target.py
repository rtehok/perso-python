from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, target):
            if node == target:
                return [[target]]

            all_paths = []

            for adj in graph[node]:
                sub_paths = dfs(adj, target)
                for sub_path in sub_paths:
                    all_paths.append([node] + sub_path)

            return all_paths

        return dfs(0, len(graph) - 1)


if __name__ == "__main__":
    assert Solution().allPathsSourceTarget([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
    assert Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4],
                                                                                     [0, 1, 2, 3, 4], [0, 1, 4]]
