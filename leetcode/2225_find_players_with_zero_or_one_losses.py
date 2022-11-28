from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = set(), defaultdict(int)
        for winner, loser in matches:
            if winner not in losers.keys():
                winners.add(winner)
            elif winner in winners:
                winners.remove(winner)

            if loser in winners:
                winners.remove(loser)

            losers[loser] += 1

        return [sorted(list(winners)), sorted([loser for loser, c in losers.items() if c == 1])]


if __name__ == "__main__":
    assert Solution().findWinners(
        [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]) == [[1, 2, 10],
                                                                                                [4, 5, 7, 8]]
    assert Solution().findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]
