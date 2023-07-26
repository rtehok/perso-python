import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right, min_speed = 1, 10_000_000, -1
        while left <= right:
            speed = (right + left) // 2
            if (sum(math.ceil(dist[i] / speed) for i in range(len(dist) - 1)) + dist[-1] / speed) > hour:
                left = speed + 1
            else:
                right = speed - 1
                min_speed = speed
        return min_speed


if __name__ == "__main__":
    assert Solution().minSpeedOnTime(dist=[1, 3, 2], hour=6) == 1
    assert Solution().minSpeedOnTime(dist=[1, 3, 2], hour=2.7) == 3
    assert Solution().minSpeedOnTime(dist=[1, 3, 2], hour=1.9) == -1
