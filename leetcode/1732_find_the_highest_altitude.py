from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = current = 0
        for i in range(len(gain)):
            current += gain[i]
            highest = max(highest, current)

        return highest


if __name__ == "__main__":
    assert Solution().largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
