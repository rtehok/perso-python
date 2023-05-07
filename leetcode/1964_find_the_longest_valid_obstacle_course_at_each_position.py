import bisect
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        res = [1] * n
        lis = []

        for i, height in enumerate(obstacles):
            idx = bisect.bisect_right(lis, height)

            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height

            res[i] = idx + 1

        return res


if __name__ == "__main__":
    assert Solution().longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]
    assert Solution().longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]
    assert Solution().longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2]
