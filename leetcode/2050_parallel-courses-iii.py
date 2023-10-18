import collections
import functools
from typing import List


class Solution:
    def minimumTimeBFSTopologicalSort(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        graph = collections.defaultdict(list)

        for (x, y) in relations:
            graph[x - 1].append(y - 1)
            indegree[y - 1] += 1

        q = collections.deque()
        max_time = [0] * n

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                max_time[i] = time[i]

        while q:
            curr = q.popleft()

            for next_course in graph[curr]:
                max_time[next_course] = max(max_time[next_course], max_time[curr] + time[next_course])

                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return max(max_time)

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        for (x, y) in relations:
            graph[x - 1].append(y - 1)

        @functools.cache
        def dfs(node):
            if not graph[node]:
                return time[node]

            ans = 0

            for next_course in graph[node]:
                ans = max(ans, dfs(next_course))

            return time[node] + ans

        ans = 0

        for node in range(n):
            ans = max(ans, dfs(node))

        return ans


if __name__ == "__main__":
    assert Solution().minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]) == 8
    assert Solution().minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]) == 12
