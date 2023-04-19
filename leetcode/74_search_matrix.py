from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrixV1(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        row = 0
        for i in range(m):
            if target in (matrix[i][0], matrix[i][-1]):
                return True
            elif matrix[i][0] < target < matrix[i][-1]:
                row = i
                break

        def find(l, r):
            while l <= r:
                mid = r - (r - l) // 2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        return find(0, n - 1)

    # O(log(m * n))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def find(l, r):
            while l <= r:
                mid = r - (r - l) // 2
                num = matrix[mid // n][mid % n]  # align all rows into single one
                if num == target:
                    return True
                if num < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        return find(0, (m * n) - 1)


if __name__ == "__main__":
    assert Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert not Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
