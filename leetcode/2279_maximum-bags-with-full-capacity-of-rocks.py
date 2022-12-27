from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0

        remainder = sorted([c - rocks[i] for i, c in enumerate(capacity)])

        for r in remainder:
            if r == 0:
                res += 1
                continue
            if r <= additionalRocks:
                res += 1
                additionalRocks -= r

        return res


if __name__ == "__main__":
    assert Solution().maximumBags(capacity=[2, 3, 4, 5], rocks=[1, 2, 4, 4], additionalRocks=2) == 3
    assert Solution().maximumBags(capacity=[10, 2, 2], rocks=[2, 2, 0], additionalRocks=100) == 3
    assert Solution().maximumBags(
        capacity=[54, 18, 91, 49, 51, 45, 58, 54, 47, 91, 90, 20, 85, 20, 90, 49, 10, 84, 59, 29, 40, 9, 100, 1, 64, 71,
                  30, 46, 91],
        rocks=
        [14, 13, 16, 44, 8, 20, 51, 15, 46, 76, 51, 20, 77, 13, 14, 35, 6, 34, 34, 13, 3, 8, 1, 1, 61, 5, 2, 15, 18],
        additionalRocks=77
    ) == 13
