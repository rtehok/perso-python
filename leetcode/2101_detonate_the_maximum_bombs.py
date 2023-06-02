import collections
from typing import List


class Solution:
    def maximumDetonationDFS(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def dfs(cur, visit):
            visit.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visit:
                    dfs(neighbor, visit)
            return len(visit)

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i, set()))

        return ans

    def maximumDetonationDFSIterative(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def dfs(i):
            stack = [i]
            visit = {i}
            while stack:
                cur = stack.pop()
                for neighbor in graph[cur]:
                    if neighbor not in visit:
                        stack.append(neighbor)
                        visit.add(neighbor)
            return len(visit)

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def bfs(i):
            q = collections.deque()
            q.append(i)
            visit = {i}
            while q:
                cur = q.popleft()
                for neighbor in graph[cur]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.append(neighbor)
            return len(visit)

        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))

        return ans


if __name__ == "__main__":
    assert Solution().maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2
    assert Solution().maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1
    assert Solution().maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
