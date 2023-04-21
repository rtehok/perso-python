from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        # Create visited matrices for Pacific and Atlantic
        pacific_visited = [[False for _ in range(n)] for _ in range(m)]
        atlantic_visited = [[False for _ in range(n)] for _ in range(m)]

        # DFS for cells that can flow to Pacific
        def dfs(i, j, visit):
            visit[i][j] = True
            # coming from pacific or atlantic, you can visit next cell if this is higher or equal
            if i - 1 >= 0 and not visit[i - 1][j] and heights[i - 1][j] >= heights[i][j]:
                dfs(i - 1, j, visit)
            if i + 1 < m and not visit[i + 1][j] and heights[i + 1][j] >= heights[i][j]:
                dfs(i + 1, j, visit)
            if j - 1 >= 0 and not visit[i][j - 1] and heights[i][j - 1] >= heights[i][j]:
                dfs(i, j - 1, visit)
            if j + 1 < n and not visit[i][j + 1] and heights[i][j + 1] >= heights[i][j]:
                dfs(i, j + 1, visit)

        # DFS from border cells to mark reachable cells
        for i in range(m):
            dfs(i, 0, pacific_visited)
            dfs(i, n - 1, atlantic_visited)
        for j in range(n):
            dfs(0, j, pacific_visited)
            dfs(m - 1, j, atlantic_visited)

        # Find cells that can reach both Pacific and Atlantic
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])

        return result


if __name__ == "__main__":
    assert Solution().pacificAtlantic(
        [[1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
