from typing import List


class Solution:
    def numSpecialV1(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue

                good = True

                for r in range(m):
                    if r != i and mat[r][j] == 1:
                        good = False
                        break

                for c in range(n):
                    if c != j and mat[i][c] == 1:
                        good = False
                        break

                if good:
                    ans += 1
        return ans

    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_cnt = [0] * m
        col_cnt = [0] * n
        ans = 0

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_cnt[row] += 1
                    col_cnt[col] += 1

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_cnt[row] == 1 and col_cnt[col] == 1:
                        ans += 1

        return ans


assert Solution().numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
assert Solution().numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
