import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = collections.Counter(tasks)
        res = 0
        for count in counter.values():
            if count == 1:
                return -1
            if count % 3 == 0:
                res += count // 3
            else:
                res += count // 3 + 1

        return res


if __name__ == "__main__":
    assert Solution().minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
    assert Solution().minimumRounds([2, 3, 3]) == -1
    assert Solution().minimumRounds([7, 7, 7, 7, 7, 7]) == 2
    assert Solution().minimumRounds([7, 7, 7, 7, 7, 7, 7, 7]) == 3
    assert Solution().minimumRounds(
        [69, 65, 62, 64, 70, 68, 69, 67, 60, 65, 69, 62, 65, 65, 61, 66, 68, 61, 65, 63, 60, 66, 68, 66, 67, 65, 63, 65,
         70, 69, 70, 62, 68, 70, 60, 68, 65, 61, 64, 65, 63, 62, 62, 62, 67, 62, 62, 61, 66, 69]) == 20
