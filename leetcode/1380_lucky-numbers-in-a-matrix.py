from typing import List


class Solution:
    def luckyNumbersV1(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        max_col = []
        for j in range(n):
            maxi = 0
            for i in range(m):
                maxi = max(maxi, matrix[i][j])
            max_col.append(maxi)

        for i in range(m):
            row = matrix[i]
            min_row = min(row)
            for j in range(n):
                if matrix[i][j] == min_row and matrix[i][j] == max_col[j]:
                    res.append(matrix[i][j])

        return res

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        r_min_max = float("-inf")
        for i in range(m):
            r_min = min(matrix[i])
            r_min_max = max(r_min_max, r_min)

        c_max_min = float("inf")
        for j in range(n):
            c_max = max(matrix[i][j] for i in range(m))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []


assert Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]) == [15]
assert Solution().luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]) == [12]
assert Solution().luckyNumbers(matrix=[[7, 8], [1, 2]]) == [7]
