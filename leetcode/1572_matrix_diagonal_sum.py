from typing import List


class Solution:
    def diagonalSumV1(self, mat: List[List[int]]) -> int:
        n = len(mat)
        i, j = 0, 0
        if n == 1:
            return mat[0][0]

        ans = 0
        while i < n:
            ans += mat[i][j]
            i += 1
            j += 1

        i, j = 0, n - 1
        while i < n:
            ans += mat[i][j]
            i += 1
            j -= 1

        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]

        return ans

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[n - 1 - i][i]

        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]

        return ans


if __name__ == "__main__":
    assert Solution().diagonalSum([[1, 2, 3],
                                   [4, 5, 6],
                                   [7, 8, 9]]) == 25
    assert Solution().diagonalSum([[1, 1, 1, 1],
                                   [1, 1, 1, 1],
                                   [1, 1, 1, 1],
                                   [1, 1, 1, 1]]) == 8
    assert Solution().diagonalSum([[5]]) == 5
