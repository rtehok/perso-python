import heapq
from typing import List


class Solution:
    def eliminateMaximumGreedy(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)

        arrival = []  # time of arrival

        for i in range(n):
            arrival.append(dist[i] / speed[i])

        arrival.sort()
        ans = 0

        for i in range(n):
            if arrival[i] <= i:
                break

            ans += 1

        return ans

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        h = []

        for i in range(len(dist)):
            heapq.heappush(h, dist[i] / speed[i])

        ans = 0

        while h:
            if heapq.heappop(h) <= ans:
                break

            ans += 1

        return ans


if __name__ == "__main__":
    assert Solution().eliminateMaximum(dist=[3, 3, 5, 7, 7], speed=[1, 1, 4, 2, 2]) == 4
    assert Solution().eliminateMaximum(dist=[4, 3, 4], speed=[1, 1, 2]) == 3
    assert Solution().eliminateMaximum(dist=[4, 2, 8], speed=[2, 1, 4]) == 2
    assert Solution().eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]) == 3
    assert Solution().eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]) == 1
    assert Solution().eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]) == 1
