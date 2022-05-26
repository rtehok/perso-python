from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        start = 0
        i = 0
        j = 0
        up, down, right, left = 0, n, n, -1

        direction = "right"

        while start < n * n:
            if direction == "right":
                while j < right and start != n * n:
                    matrix[i][j] = start + 1
                    j += 1
                    start += 1
                direction = "down"
                right -= 1
                j -= 1
                i += 1
            if direction == "down":
                while i < down and start != n * n:
                    matrix[i][j] = start + 1
                    i += 1
                    start += 1
                direction = "left"
                down -= 1
                i -= 1
                j -= 1
            if direction == "left":
                while j > left and start != n * n:
                    matrix[i][j] = start + 1
                    j -= 1
                    start += 1
                direction = "up"
                left += 1
                j += 1
                i -= 1
            if direction == "up":
                while i > up and start != n * n:
                    matrix[i][j] = start + 1
                    i -= 1
                    start += 1
                direction = "right"
                up += 1
                i += 1
                j += 1

        return matrix


if __name__ == "__main__":
    # print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(5))
