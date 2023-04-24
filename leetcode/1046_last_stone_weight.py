import heapq
from typing import List


class Solution:
    def lastStoneWeightV1(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones = stones[2:]
                stones.append(0)
            else:
                diff = stones[0] - stones[1]
                stones = stones[2:]
                stones.append(diff)
                stones.sort(reverse=True)

        return stones[0]

    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h) > 1:
            stone1 = heapq.heappop(h)
            stone2 = heapq.heappop(h)
            if stone1 != stone2:
                heapq.heappush(h, stone1 - stone2)

        return 0 if not h else -heapq.heappop(h)


if __name__ == "__main__":
    assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert Solution().lastStoneWeight([1]) == 1
    assert Solution().lastStoneWeight([2, 2]) == 0
