import collections
import functools
import math


class Solution:
    # TC O(k * n**2) / SC O(k * n ** 2)
    def knightProbabilityBottomUp(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]

        dp[0][row][column] = 1

        for move in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for dir in moves:
                        prev_i, prev_j = i - dir[0], j - dir[1]
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            dp[move][i][j] += dp[move - 1][prev_i][prev_j] / 8

        total_proba = sum([dp[k][i][j] for i in range(n) for j in range(n)])

        return total_proba

    # TC O(k * n**2) / SC O(n ** 2)
    def knightProbabilityBottomUpSpaceOptimized(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        prev_dp = [[0] * n for _ in range(n)]
        curr_dp = [[0] * n for _ in range(n)]

        prev_dp[row][column] = 1

        for move in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    curr_dp[i][j] = 0  # reset current cell
                    for dir in moves:
                        prev_i, prev_j = i - dir[0], j - dir[1]
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            curr_dp[i][j] += prev_dp[prev_i][prev_j] / 8

            prev_dp, curr_dp = curr_dp, prev_dp

        total_proba = sum([prev_dp[i][j] for i in range(n) for j in range(n)])

        return total_proba

    def knightProbabilityTopDown(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        dp = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]

        def dfs(moves, i, j):
            if moves == 0:
                if i == row and j == column:
                    return 1
                else:
                    return 0

            if dp[moves][i][j] != -1:
                return dp[moves][i][j]

            dp[moves][i][j] = 0  # reset current cell

            for dx, dy in directions:
                px, py = i - dx, j - dy
                if 0 <= px < n and 0 <= py < n:
                    dp[moves][i][j] += dfs(moves - 1, px, py) / 8

            return dp[moves][i][j]

        return sum([dfs(k, i, j) for i in range(n) for j in range(n)])

    # BFS + DP
    def knightProbabilityBFS(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        q = collections.defaultdict(int)
        q[row, column] = 1
        p = 1
        for _ in range(k):
            p = 0  # reset current cell proba
            next_q = collections.defaultdict(int)
            for (r, c), rcp in q.items():
                for dr, dc in directions:
                    if n > (nr := dr + r) >= 0 <= (nc := dc + c) < n:
                        next_q[nr, nc] += rcp / 8  # DP
                        p += rcp / 8
            q = next_q

        return p

    def knightProbabilityDFS(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        @functools.cache
        def calculate_proba(r, c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1

            return sum(calculate_proba(r + dr, c + dc, k - 1) for dr, dc in moves) / 8

        return calculate_proba(row, column, k)

    def knightProbabilityDFSTopBottom(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        dp = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]

        dp[0][row][column] = 1

        def calculate_proba(r, c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1

            if dp[k][r][c] != -1:
                return dp[k][r][c]

            dp[k][r][c] = 0

            for dr, dc in moves:
                dp[k][r][c] += calculate_proba(r + dr, c + dc, k - 1) / 8

            return dp[k][r][c]

        return calculate_proba(row, column, k)

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        mid = math.ceil(n / 2)

        @functools.cache
        def calculate_proba(r, c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1

            if r > c or r >= mid or c >= mid:
                if r > c:
                    r, c = c, r
                r, c = min(r, n - 1 - r), min(c, n - 1 - c)
                return calculate_proba(r, c, k)

            return sum(calculate_proba(r + dr, c + dc, k - 1) for dr, dc in moves) / 8

        return calculate_proba(row, column, k)


if __name__ == "__main__":
    assert Solution().knightProbability(n=3, k=2, row=0, column=0) == 0.06250
    assert Solution().knightProbability(n=1, k=0, row=0, column=0) == 1
