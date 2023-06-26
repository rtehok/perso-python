import collections
import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        next_head, next_tail = candidates, n - 1 - candidates
        ans = 0

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                ans += heapq.heappop(head_workers)

                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                ans += heapq.heappop(tail_workers)

                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return ans


if __name__ == "__main__":
    assert Solution().totalCost(costs=[1, 2, 4, 1], k=3, candidates=3) == 4
    assert Solution().totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4) == 11
    assert Solution().totalCost([31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], k=11,
                                candidates=2) == 423
