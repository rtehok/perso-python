from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0]:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, m):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1 else 0

        for j in range(1, n):
            obstacleGrid[0][j] = 1 if obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1 else 0

        for r in range(1, m):
            for c in range(1, n):
                obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c-1] if obstacleGrid[r][c] == 0 else 0

        return obstacleGrid[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
    print(Solution().uniquePathsWithObstacles([[1, 0]]))
    print(Solution().uniquePathsWithObstacles([[0]]))
