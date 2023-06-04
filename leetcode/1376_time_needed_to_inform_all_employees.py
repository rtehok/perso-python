import collections
from typing import List


class Solution:
    def numOfMinutesDFS(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                m = manager[i]
                graph[m].append(i)

        if n == 1:
            return 0

        max_time = float("-inf")

        def dfs(m, t):
            nonlocal max_time
            max_time = max(max_time, t)

            for e in graph[m]:
                dfs(e, t + informTime[m])

            return max_time

        return dfs(headID, 0)

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                m = manager[i]
                graph[m].append(i)

        max_time = float("-inf")

        q = collections.deque()
        q.append((headID, 0))

        while q:
            m, t = q.popleft()

            max_time = max(max_time, t)

            for e in graph[m]:
                q.append((e, t + informTime[m]))

        return max_time


if __name__ == "__main__":
    assert Solution().numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]) == 0
    assert Solution().numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]) == 1
    assert Solution().numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1],
                                   informTime=[0, 6, 5, 4, 3, 2, 1]) == 21
