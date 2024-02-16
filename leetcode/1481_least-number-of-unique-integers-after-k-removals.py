import collections
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        freq = list(cnt.values())
        freq.sort()
        elts_removed = 0
        for i in range(len(freq)):
            elts_removed += freq[i]

            if elts_removed > k:
                return len(freq) - i

        return 0


assert Solution().findLeastNumOfUniqueInts(arr=[1], k=1) == 0
assert Solution().findLeastNumOfUniqueInts(arr=[1], k=0) == 1
assert Solution().findLeastNumOfUniqueInts(arr=[1, 2, 2, 2, 2], k=2) == 1
assert Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3) == 2
assert Solution().findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1) == 1
assert Solution().findLeastNumOfUniqueInts([2, 4, 1, 8, 3, 5, 1, 3], 3) == 3
