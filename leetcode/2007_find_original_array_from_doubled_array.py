from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)

        res = []

        if n % 2 != 0:
            return res

        changed.sort()
        freq = Counter(changed)

        for x in changed:
            if freq[x] == 0:
                continue
            else:
                if freq.get(2 * x, 0) >= 1:
                    res.append(x)
                    freq[2 * x] -= 1
                    freq[x] -= 1
                else:
                    return []

        return res


if __name__ == "__main__":
    assert Solution().findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4]
