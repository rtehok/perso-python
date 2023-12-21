from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_diff = points[1][0] - points[0][0]
        for i in range(1, len(points)):
            max_diff = max(max_diff, points[i][0] - points[i - 1][0])
        return max_diff


assert Solution().maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]) == 1
assert Solution().maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3
