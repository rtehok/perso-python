import collections
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_arr = max(arr)
        curr = arr[0]
        win_streak = 0

        for i in range(1, len(arr)):
            opponent = arr[i]

            if opponent > curr:
                win_streak = 1
                curr = opponent
            else:
                win_streak += 1

            if win_streak == k or curr == max_arr:
                return curr


if __name__ == "__main__":
    assert Solution().getWinner([2, 1, 3, 5, 4, 6, 7], 2) == 5
    assert Solution().getWinner([1, 25, 35, 42, 68, 70], 1) == 25
    assert Solution().getWinner([3, 2, 1], 10) == 3
