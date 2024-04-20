from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        res = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    bottom_row = i
                    bottom_col = j

                    while bottom_row + 1 < m and land[bottom_row + 1][j] == 1:
                        bottom_row += 1
                    while bottom_col + 1 < n and land[i][bottom_col + 1] == 1:
                        bottom_col += 1

                    res.append([i, j, bottom_row, bottom_col])

        return res


assert Solution().findFarmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [[0, 0, 0, 0], [1, 1, 2, 2]]
assert Solution().findFarmland(land=[[1, 1], [1, 1]]) == [[0, 0, 1, 1]]
assert Solution().findFarmland(land = [[0]]) == []
