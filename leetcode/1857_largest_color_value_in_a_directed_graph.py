import collections
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        indegree = [0] * n  # kahn's algorithm to track cycle

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1  # count the number of ingoing

        count = [[0] * 26 for _ in range(n)]

        q = collections.deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        res = 1
        node_seen = 0
        while q:
            node = q.popleft()

            count[node][ord(colors[node]) - ord('a')] += 1
            res = max(res, count[node][ord(colors[node]) - ord('a')])

            node_seen += 1

            for neighbor in graph[node]:
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[node][i])

                indegree[neighbor] -= 1  # remove it when visiting
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return -1 if node_seen < n else res


if __name__ == "__main__":
    assert Solution().largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
    assert Solution().largestPathValue(colors="a", edges=[[0, 0]]) == -1
    assert Solution().largestPathValue(colors="hhqhuqhqff",
                                       edges=[[0, 1], [0, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7], [6, 7], [7, 8],
                                              [3, 8], [5, 8], [8, 9], [3, 9], [6, 9]]) == 3
    assert Solution().largestPathValue(colors="iivvvvv",
                                       edges=[[0, 1], [1, 2], [1, 3], [2, 3], [3, 4], [2, 4], [3, 5], [1, 5], [4, 5],
                                              [5, 6]]) == 5
