from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            tmp = board[i][j]
            board[i][j] = ""
            if dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1):
                return True
            board[i][j] = tmp

            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True

        return False


assert Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
assert Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
assert not Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
