from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasingQueue(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque()

        for i in range(n):
            q.append(i)

        deck.sort()
        res = [0] * n
        for card in deck:
            res[q.popleft()] = card

            if q:
                q.append(q.popleft())

        return res

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        res = [0] * n
        skip = False
        index_in_deck = 0
        index_in_res = 0

        deck.sort()
        while index_in_deck < n:
            if res[index_in_res] == 0:
                if not skip:
                    res[index_in_res] = deck[index_in_deck]
                    index_in_deck += 1

                skip = not skip
            index_in_res = (index_in_res + 1) % n

        return res


assert Solution().deckRevealedIncreasing(deck=[17, 13, 11, 2, 3, 5, 7]) == [2, 13, 3, 11, 5, 17, 7]
