import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # contains possible (row, col) based on value
        cells = [None] * (n ** 2 + 1)
        i = 1
        columns = list(range(n))

        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[i] = (row, column)
                i += 1
            columns.reverse()

        dist = [-1] * (n ** 2 + 1)

        q = collections.deque([1])

        dist[1] = 0

        while q:
            curr = q.popleft()
            for next_value in range(curr + 1, min(curr + 6, n ** 2) + 1):
                row, col = cells[next_value]
                # if it's a snake or ladder, need to go to the board value
                destination = board[row][col] if board[row][col] != -1 else next_value
                # update once
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    # add to queue (BFS)
                    q.append(destination)

        return dist[n * n]


if __name__ == "__main__":
    assert Solution().snakesAndLadders(
        [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]) == 4
    assert Solution().snakesAndLadders([[-1, -1], [-1, 3]]) == 1
