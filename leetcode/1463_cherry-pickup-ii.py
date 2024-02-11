from typing import List


class Solution:
    def cherryPickupRecursive(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @functools.cache
        def solve(curr_row, a_col, b_col):
            if a_col < 0 or b_col < 0 or a_col >= n or b_col >= n:
                return 0
            if curr_row == m:
                return 0

            res = 0
            res += grid[curr_row][a_col]
            res += grid[curr_row][b_col]

            child_res = 0
            for a in [a_col - 1, a_col, a_col + 1]:
                for b in [b_col - 1, b_col, b_col + 1]:
                    if a < b:
                        child_res = max(child_res, solve(curr_row + 1, a, b))

            res += child_res
            return res
        return solve(0, 0, n - 1)

    def cherryPickupTopDown(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(m)]

        def solve(curr_row, a_col, b_col):
            if a_col < 0 or b_col < 0 or a_col >= n or b_col >= n:
                return 0
            if curr_row == m:
                return 0

            if memo[curr_row][a_col][b_col] != -1:
                return memo[curr_row][a_col][b_col]

            res = 0
            res += grid[curr_row][a_col]
            res += grid[curr_row][b_col]

            child_res = 0
            for a in [a_col - 1, a_col, a_col + 1]:
                for b in [b_col - 1, b_col, b_col + 1]:
                    if a < b:
                        child_res = max(child_res, solve(curr_row + 1, a, b))

            res += child_res
            memo[curr_row][a_col][b_col] = res

            return res
        return solve(0, 0, n - 1)

    def cherryPickupBottomUp(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][-1] = grid[0][0] + grid[0][-1]

        for curr_row in range(1, m):
            for a_col in range(n):
                for b_col in range(a_col + 1, n):
                    for a in [a_col - 1, a_col, a_col + 1]:
                        for b in [b_col - 1, b_col, b_col + 1]:
                            if 0 <= a < n and 0 <= b < n:
                                prev = dp[curr_row - 1][a][b]
                                if prev != -1:
                                    dp[curr_row][a_col][b_col] = max(dp[curr_row][a_col][b_col],
                                                                     prev + grid[curr_row][a_col] + (grid[curr_row][b_col] if a_col != b_col else 0))

        ans = max(max(row) for row in dp[-1])
        return ans if ans != -1 else 0

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(2)]
        dp[0][0][-1] = grid[0][0] + grid[0][-1]

        ans = -1

        for curr_row in range(1, m):
            for a_col in range(n):
                for b_col in range(a_col + 1, n):
                    max_res = -1
                    for a in [a_col - 1, a_col, a_col + 1]:
                        for b in [b_col - 1, b_col, b_col + 1]:
                            if 0 <= a < n and 0 <= b < n:
                                max_res = max(max_res, dp[(curr_row + 1) % 2][a][b])
                    if max_res != -1:
                        dp[curr_row % 2][a_col][b_col] = max_res + grid[curr_row][a_col] + grid[curr_row][b_col]

                    ans = max(ans, dp[curr_row % 2][a_col][b_col])

        return ans


assert Solution().cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]) == 24
assert Solution().cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]) == 28