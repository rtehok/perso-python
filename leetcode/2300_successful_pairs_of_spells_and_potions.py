import bisect
import math
from typing import List


class Solution:
    def successfulPairsV1(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        m, n = len(spells), len(potions)

        def find(spell):
            left, right = 0, n - 1
            while left <= right:
                mid = right - (right - left) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        res = []

        for spell in spells:
            res.append(n - find(spell))

        return res

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        res = []

        max_potion = potions[-1]

        for spell in spells:

            min_potion = math.ceil(success / spell)

            if min_potion > max_potion:
                res.append(0)
                continue

            index = bisect.bisect_left(potions, min_potion)
            res.append(len(potions) - index)

        return res


if __name__ == "__main__":
    assert Solution().successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16) == [2, 0, 2]
    assert Solution().successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7) == [4, 0, 3]
