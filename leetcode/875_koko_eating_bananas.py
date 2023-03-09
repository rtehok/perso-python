import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate_eating_bananas):
            total_hr = 0
            for pile in piles:
                total_hr += math.ceil(pile / rate_eating_bananas)

            return total_hr <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    assert Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23
