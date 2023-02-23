import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()

        q = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:  # min_capital <= current_capital
                heapq.heappush(q, -projects[i][1])  # order in reverse to maximize profit
                i += 1
            if not q:
                break
            w += -heapq.heappop(q)  # take the max profit
        return w


if __name__ == "__main__":
    assert Solution().findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]) == 4
    assert Solution().findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]) == 6
