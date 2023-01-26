import collections
import math
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(set)
        for a, b, price in flights:
            graph[a].add((b, price))

        q = collections.deque([(src, 0)])

        prices = [math.inf] * n
        stops = 0

        while q and stops <= k:
            for _ in range(len(q)):  # this is necessary for example 2, you want to get the minimal cost, if <= k
                node, cumulated_cost = q.popleft()
                for neighbor, price in graph[node]:
                    if price + cumulated_cost >= prices[neighbor]:
                        continue
                    prices[neighbor] = price + cumulated_cost
                    q.append((neighbor, prices[neighbor]))
            stops += 1

        return -1 if prices[dst] == math.inf else prices[dst]


if __name__ == "__main__":
    assert Solution().findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                                        src=0, dst=3, k=1) == 700
    assert Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1) == 200
    assert Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0) == 500
