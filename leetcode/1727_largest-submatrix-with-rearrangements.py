from typing import List


class Solution:
    def largestSubmatrixV1(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr_row = sorted(matrix[row], reverse=True)
            for i in range(n):
                ans = max(ans, curr_row[i] * (i + 1))

        return ans

    def largestSubmatrixNoSort(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        prev_row = [0] * n

        for row in range(m):
            curr_row = matrix[row][:]
            for col in range(n):
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]
            sorted_row = sorted(curr_row, reverse=True)

            for i in range(n):
                ans = max(ans, sorted_row[i] * (i + 1))

            prev_row = curr_row

        return ans

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        prev_heights = []

        for row in range(m):
            heights = []
            seen = [False] * n

            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))  # manual sort
                    seen[col] = True

            for col in range(n):
                if not seen[col] and matrix[row][col] == 1:
                    heights.append((1, col))

            for i in range(len(heights)):
                ans = max(ans, heights[i][0] * (i + 1))

            prev_heights = heights

        return ans


if __name__ == "__main__":
    assert Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
    assert Solution().largestSubmatrix([[1, 0, 1, 0, 1]]) == 3
    assert Solution().largestSubmatrix(matrix=[[1, 1, 0], [1, 0, 1]]) == 2
