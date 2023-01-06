from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # sort by the end asc

        res, current_end = 1, points[0][1]

        for start, end in points:
            if start > current_end:
                res += 1
                current_end = end

        return res


if __name__ == "__main__":
    assert Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
