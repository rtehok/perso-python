from heapq import heappush, heappop
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        for pile in piles:
            heappush(h, -pile)

        while k >= 1:
            greatest = heappop(h)
            heappush(h, greatest // 2)

            k -= 1

        return -sum(h)


if __name__ == "__main__":
    assert Solution().minStoneSum(piles=[5, 4, 9], k=2) == 12
    assert Solution().minStoneSum(piles=[4, 3, 6, 7], k=3) == 12
