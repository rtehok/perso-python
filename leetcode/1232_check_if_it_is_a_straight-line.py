from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        x2, y2 = coordinates[1]
        x1, y1 = coordinates[0]
        previous_slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float("inf")

        for i in range(2, n):
            x2, y2 = coordinates[i]
            x1, y1 = coordinates[i - 1]
            slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float("inf")
            if previous_slope != slope:
                return False

            previous_slope = slope

        return True


if __name__ == "__main__":
    assert Solution().checkStraightLine([[2, 4], [2, 5], [2, 8]])
    assert Solution().checkStraightLine([[0, 0], [0, 1], [0, -1]])
    assert not Solution().checkStraightLine([[1, 2], [2, 3], [3, 5]])
    assert Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    assert not Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
    assert not Solution().checkStraightLine([[0, 0], [0, 5], [5, 5], [5, 0]])
    assert Solution().checkStraightLine([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]])
