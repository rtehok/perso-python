from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for x in arr:
            d[x] += 1

        tmp = [a for k, a in d.items()]

        return len(tmp) == len(set(tmp))


if __name__ == "__main__":
    assert Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3])
    assert not Solution().uniqueOccurrences([1, 2])
    assert Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
