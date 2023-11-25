import collections
from typing import List


class Solution:
    def maxCoinsV1(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        i = 1
        while i <= len(piles):
            ans += piles[i]
            i += 2
            piles.pop()
        return ans

    def maxCoinsNoQueue(self, piles: List[int]) -> int:
        piles.sort()

        ans = 0

        for i in range(len(piles) // 3, len(piles), 2):
            ans += piles[i]

        return ans

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = collections.deque(piles)
        ans = 0
        while q:
            q.pop()
            ans += q.pop()
            q.popleft()

        return ans


if __name__ == "__main__":
    assert Solution().maxCoins(piles=[2, 4, 1, 2, 7, 8]) == 9
    assert Solution().maxCoins(piles=[2, 4, 5]) == 4
    assert Solution().maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18
