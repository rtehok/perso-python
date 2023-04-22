import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = collections.defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)  # stop -> { bus number }

        res = -1
        visit = set()

        q = collections.deque()
        q.append(source)

        while q:
            res += 1
            for _ in range(len(q)):
                current_stop = q.popleft()
                if current_stop == target:
                    return res
                for bus in graph[current_stop]:
                    if bus not in visit:
                        visit.add(bus)  # consider bus as a node
                        q.extend(routes[bus])  # extend not add
        return -1


if __name__ == "__main__":
    assert Solution().numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6) == 2
    assert Solution().numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15,
                                            target=12) == -1
