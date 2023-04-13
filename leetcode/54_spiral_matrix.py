from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, down = 1, 0
        row, col = 0, 0
        m, n = len(matrix), len(matrix[0])
        res = []
        limit_up, limit_down = 0, m - 1
        limit_left, limit_right = 0, n - 1

        while limit_up <= limit_down and limit_left <= limit_right:
            res.append(matrix[row][col])

            # going left
            if left == 1 and col == limit_right:
                left = 0
                down = 1
                limit_up += 1

            # going down
            if down == 1 and row == limit_down:
                down = 0
                left = -1
                limit_right -= 1

            # going left
            if left == -1 and col == limit_left:
                left = 0
                down = -1
                limit_down -= 1

            # going up
            if down == -1 and row == limit_up:
                down = 0
                left = 1
                limit_left += 1

            col += left
            row += down

        return res


if __name__ == "__main__":
    assert Solution().spiralOrder([[1]]) == [1]
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6,
                                                                                     7]
    assert Solution().spiralOrder([[2, 5], [8, 4], [0, -1]]) == [2, 5, 4, -1, 0, 8]
    assert Solution().spiralOrder([[3], [2]]) == [3, 2]
