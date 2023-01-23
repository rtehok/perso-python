from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trusts = [0] * (n + 1)

        for a, b in trust:
            trusted[b] += 1
            trusts[a] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i

        return -1


if __name__ == "__main__":
    assert Solution().findJudge(2, [[1, 2]]) == 2
    assert Solution().findJudge(3, [[1, 3], [2, 3]]) == 3
    assert Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
    assert Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
    assert Solution().findJudge(3, [[1, 2], [2, 3]]) == -1
