import collections
import math
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)

        for a, b, score in roads:
            graph[a].add((b, score))
            graph[b].add((a, score))

        res = math.inf

        q = collections.deque()
        q.append(1)

        visited = {1}

        while q:
            q_len = len(q)

            while q_len:
                node = q.popleft()

                for child, score in graph[node]:
                    res = min(res, score)
                    if child not in visited:
                        visited.add(child)
                        q.append(child)

                q_len -= 1

        return res


if __name__ == "__main__":
    assert Solution().minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5
    assert Solution().minScore(n=4, roads=[[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2
