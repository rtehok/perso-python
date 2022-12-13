from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        for i in range(1, n):
            matrix[i][0] = matrix[i][0] + min(matrix[i - 1][0], matrix[i - 1][1])
            matrix[i][-1] = matrix[i][-1] + min(matrix[i - 1][-2], matrix[i - 1][-1])
            for j in range(1, n - 1):
                matrix[i][j] = matrix[i][j] + min([matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1]])

        return min(matrix[-1])


if __name__ == "__main__":
    assert Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert Solution().minFallingPathSum([[-19, 57], [-40, -5]]) == -59
    assert Solution().minFallingPathSum([[42]]) == 42
    assert Solution().minFallingPathSum([[-80, -13, 22], [83, 94, -5], [73, -48, 61]]) == -66
