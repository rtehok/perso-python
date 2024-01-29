import collections
from typing import List


class Solution:
    def numSubmatrixSumTargetBruteForce(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])

        def sum_sub_matrix(row_start, row_size, col_start, col_size):
            sub_matrix_sum = 0
            for i in range(row_start, row_start + row_size):
                for j in range(col_start, col_start + col_size):
                    sub_matrix_sum += matrix[i][j]
            return sub_matrix_sum

        for row_start in range(m):
            for row_size in range(1, m - row_start + 1):
                for col_start in range(0, n):
                    for col_size in range(1, n - col_start + 1):
                        if sum_sub_matrix(row_start, row_size, col_start, col_size) == target:
                            ans += 1
        return ans

    def numSubmatrixSumTargetPrefixSum(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]  # calculate prefix sum for each row

        for col_start in range(n):
            for col_end in range(col_start, n):
                for row_start in range(m):
                    sum = 0
                    for row_end in range(row_start, m):
                        sum += matrix[row_end][col_end] - (matrix[row_end][col_start - 1] if col_start > 0 else 0)
                        if sum == target:
                            ans += 1

        return ans

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]  # calculate prefix sum for each row

        for col_start in range(n):
            for col_end in range(col_start, n):
                cnt = collections.defaultdict(int)
                cnt[0] = 1
                sum = 0
                for row in range(m):
                    sum += matrix[row][col_end] - (matrix[row][col_start - 1] if col_start > 0 else 0)
                    ans += cnt[sum - target]
                    cnt[sum] += 1

        return ans


assert Solution().numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0) == 4
assert Solution().numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0) == 5
