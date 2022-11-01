from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        res = []
        for col in range(n):
            current_col = col
            for current_row in range(m):
                # going right: col 0 + 1 = col 1
                # going left: col 3 - 1 = col 2
                next_col = current_col + grid[current_row][current_col]
                # cannot go outside the grid
                # the ball is stuck at a V shape position
                # e.g. ball 2 and ball 3 in column 2 and column 3 in row 0
                # hence, we check if the grid[cur_row][cur_col] is different from grid[cur_row][next_col]
                if next_col < 0 or next_col >= n or grid[current_row][current_col] != grid[current_row][next_col]:
                    current_col = -1
                    break

                current_col = next_col
            # the ball reaches to the end current_col is the final destination
            res.append(current_col)

        return res


if __name__ == "__main__":
    assert Solution().findBall(
        [[1, 1, 1, -1, -1],
         [1, 1, 1, -1, -1],
         [-1, -1, -1, 1, 1],
         [1, 1, 1, 1, -1],
         [-1, -1, -1, -1, -1]
         ]) == [1, -1, -1, -1, -1]

    assert Solution().findBall(
        [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
    ) == [0, 1, 2, 3, 4, -1]
