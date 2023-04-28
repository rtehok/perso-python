import collections
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        visit = [False] * n

        def isSimilar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
            return diff == 0 or diff == 2

        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node):
            visit[node] = True
            if node not in graph:
                return

            for neighbor in graph[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                count += 1

        return count


if __name__ == "__main__":
    assert Solution().numSimilarGroups(["tars", "rats", "arts", "star"]) == 2
    assert Solution().numSimilarGroups(["omv", "ovm"]) == 1
