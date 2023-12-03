from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))

        return ans


if __name__ == "__main__":
    assert Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]) == 7
    assert Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]) == 5
