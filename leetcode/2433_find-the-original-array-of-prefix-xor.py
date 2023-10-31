from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i - 1] ^ pref[i] for i in range(1, len(pref))]


if __name__ == "__main__":
    assert Solution().findArray(pref=[5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]
    assert Solution().findArray(pref=[13]) == [13]
