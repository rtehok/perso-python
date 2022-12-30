from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = "#"

                for r, c in moves:
                    x = i + r
                    y = j + c
                    if 0 <= x < m and 0 <= y < n:
                        dfs(x, y)

        def bfs(i, j):
            level = [(i, j)]
            while level:
                tmp = []
                for i, j in level:
                    if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                        board[i][j] = '#'
                        tmp += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    level = tmp

        # First pass: change O to # for borders and island connected to border
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in {0, m - 1} or j in {0, n - 1}):
                    # dfs(i, j)
                    bfs(i, j)

        # Second pass: change # to O for borders, if O not touched, then replace by X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


if __name__ == "__main__":
    a = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    Solution().solve(a)
    assert a == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    a = [['X']]
    Solution().solve(a)
    assert a == [['X']]

    a = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    Solution().solve(a)
    assert a == [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

    a = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    Solution().solve(a)
    assert a == [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
