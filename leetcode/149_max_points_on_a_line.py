from typing import List
import collections

import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calc_slope(x1, y1, x2, y2):
            return (y2-y1) / (x2 - x1) if x2 != x1 else math.inf

        res = 1
        n = len(points)

        for i in range(n):
            slopes = collections.Counter()
            max_points = 1

            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                slope = calc_slope(x1, y1, x2, y2)
                slopes[slope] += 1
                max_points = max(max_points, 1 + slopes[slope])
            res = max(res, max_points)

        return res


if __name__ == "__main__":
    assert Solution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
