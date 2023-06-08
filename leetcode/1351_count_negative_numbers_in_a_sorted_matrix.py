from typing import List


class Solution:
    def countNegativesV1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] < 0:
                    cnt += 1
                else:
                    break

        return cnt

    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid[0])
        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = (right + left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            cnt += n - left
        return cnt


if __name__ == "__main__":
    assert Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
    assert Solution().countNegatives([[3, 2], [1, 0]]) == 0
