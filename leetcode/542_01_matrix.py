import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[math.inf] * len(mat[0]) for _ in range(len(mat))]

        # init
        if mat[0][0] == 0:
            dist[0][0] = 0

        # top -> bottom
        # left -> right
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                elif i > 0 and j > 0:
                    dist[i][j] = 1 + min(dist[i - 1][j], dist[i][j - 1])
                elif i > 0:
                    dist[i][j] = 1 + dist[i - 1][j]
                else:
                    dist[i][j] = 1 + dist[i][j - 1]

        # bottom -> top
        # right -> left
        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[0]) - 1, -1, -1):
                if i < len(mat) - 1 and j < len(mat[0]) - 1:
                    dist[i][j] = min(1 + min(dist[i + 1][j], dist[i][j + 1]),
                                     dist[i][j])  # compare with previously found result
                elif i < len(mat) - 1:
                    dist[i][j] = min(1 + dist[i + 1][j], dist[i][j])
                elif j < len(mat[0]) - 1:
                    dist[i][j] = min(1 + dist[i][j + 1], dist[i][j])

        return dist


if __name__ == "__main__":
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
