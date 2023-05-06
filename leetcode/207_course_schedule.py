import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)

        in_degree = [0] * numCourses
        for course, _ in prerequisites:
            in_degree[course] += 1

        count = 0

        q = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            course = q.popleft()
            count += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses


if __name__ == "__main__":
    assert Solution().canFinish(numCourses=2, prerequisites=[[1, 0]])
    assert not Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
