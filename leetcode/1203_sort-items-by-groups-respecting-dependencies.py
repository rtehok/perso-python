import collections
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topologicalSort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]

            while stack:
                curr = stack.pop()
                visited.append(curr)

                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        stack.append(neighbor)

            return visited if len(visited) == len(graph) else []

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        res = []
        for group_index in group_order:
            res += ordered_groups[group_index]

        return res


if __name__ == "__main__":
    assert Solution().sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
                                beforeItems=[[], [6], [5], [6], [3, 6], [], [], []]) == [7, 0, 5, 2, 6, 3, 4, 1]
    assert Solution().sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
                                beforeItems=[[], [6], [5], [6], [3], [], [4], []]) == []
