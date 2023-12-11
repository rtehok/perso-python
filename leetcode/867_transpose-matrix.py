from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[] for _ in range(n)]
        for j in range(n):
            for i in range(m):
                res[j].append(matrix[i][j])

        return res
        # [(0, 0), (1, 0), (2, 0)]
        # [(0, 1), (1, 1), (2, 1)]
        # [(0, 2), (1, 2), (2, 2)]

        # [(0, 0), (1, 0)]
        # [(0, 1), (1, 1)]
        # [(0, 2), (1, 2)]


if __name__ == "__main__":
    assert Solution().transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert Solution().transpose(matrix=[[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
