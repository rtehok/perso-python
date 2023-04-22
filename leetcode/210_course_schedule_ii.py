import collections
from typing import List


class Solution:
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visit = [0] * numCourses

        res = []

        def dfs(course):
            visit[course] = True
            for neighbor in graph[course]:
                if visit[neighbor] == 1:
                    return False
                elif visit[neighbor] == 0:
                    if not dfs(neighbor):
                        return False

            visit[course] = 2
            res.append(course)
            return True

        for i in range(numCourses):
            if visit[i] == 0:
                if not dfs(i):
                    return []  # cycle detected

        return res[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(res) == numCourses:
            return res
        else:
            return []


if __name__ == "__main__":
    assert Solution().findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert Solution().findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) in (
        [0, 2, 1, 3], [0, 1, 2, 3])
    assert Solution().findOrder(numCourses=1, prerequisites=[]) == [0]
    assert Solution().findOrder(numCourses=2, prerequisites=[]) in ([0, 1], [1, 0])
