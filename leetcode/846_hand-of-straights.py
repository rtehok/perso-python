import collections
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        hand.sort()
        cnt = collections.Counter(hand)

        for num in hand:
            if cnt[num]:
                for cur in range(num, num + groupSize):
                    cnt[cur] -= 1
                    if cnt[cur] < 0:
                        return False

        return True


assert Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
assert not Solution().isNStraightHand(hand=[8, 10, 12], groupSize=3)
assert not Solution().isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4)
