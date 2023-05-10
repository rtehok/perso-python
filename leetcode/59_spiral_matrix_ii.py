import math
from typing import List


class Solution:
    def generateMatrixV1(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        right, down = 1, 0
        limit_left, limit_right = 0, n - 1
        limit_up, limit_down = 0, n - 1
        row, col = 0, 0
        i = 1
        while limit_left <= limit_right and limit_up <= limit_down:
            ans[row][col] = i

            if right == 1 and col == limit_right:
                right = 0
                down = 1
                limit_up += 1

            if down == 1 and row == limit_down:
                right = -1
                down = 0
                limit_right -= 1

            if right == -1 and col == limit_left:
                right = 0
                down = -1
                limit_down -= 1

            if down == -1 and row == limit_up:
                right = 1
                down = 0
                limit_left += 1

            col += right
            row += down

            i += 1

        return ans

    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        cnt = 1
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction = 0
        row, col = 0, 0
        while cnt <= n ** 2:
            ans[row][col] = cnt
            cnt += 1
            r = (row + moves[direction][0]) % n  # next row
            c = (col + moves[direction][1]) % n  # next col

            if ans[r][c] != 0:
                direction = (direction + 1) % 4

            row += moves[direction][0]
            col += moves[direction][1]

        return ans


if __name__ == "__main__":
    assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
