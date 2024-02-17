import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(pq, diff)  # push to min heap so that you use ladders for larger jumps

            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)  # use ladder, keep bricks for smaller jumps

            if bricks < 0:
                return i

        return n - 1


assert Solution().furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
assert Solution().furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
assert Solution().furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
