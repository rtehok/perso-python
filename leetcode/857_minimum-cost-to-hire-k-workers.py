import heapq
import math
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        total_cost = float("inf")
        current_total_quality = 0
        wage_to_quality_ratio = []

        for i in range(n):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        wage_to_quality_ratio.sort()

        highest_quality_worker = []

        for i in range(n):
            heapq.heappush(highest_quality_worker, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            if len(highest_quality_worker) > k:
                current_total_quality += heapq.heappop(highest_quality_worker)

            if len(highest_quality_worker) == k:
                total_cost = min(total_cost,
                                 current_total_quality * wage_to_quality_ratio[i][0])

        return total_cost


assert Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2) == 105.00000
assert math.isclose(Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3), 30.66667, rel_tol=1e-5)
