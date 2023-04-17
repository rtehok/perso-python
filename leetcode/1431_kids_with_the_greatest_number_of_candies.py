from typing import List


class Solution:
    def maxCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [candy + extraCandies >= m for candy in candies]


if __name__ == "__main__":
    assert Solution().maxCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]
    assert Solution().maxCandies(candies=[4, 2, 1, 1, 2], extraCandies=1) == [True, False, False, False, False]
    assert Solution().maxCandies(candies=[12, 1, 12], extraCandies=10) == [True, False, True]
