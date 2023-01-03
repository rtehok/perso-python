from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])

        res = 0

        for col in range(n):
            for i in range(1, m):
                if strs[i - 1][col] > strs[i][col]:
                    res += 1
                    break
        return res


if __name__ == "__main__":
    assert Solution().minDeletionSize(["cba", "daf", "ghi"]) == 1
    assert Solution().minDeletionSize(["a", "b"]) == 0
    assert Solution().minDeletionSize(["zyx", "wvu", "tsr"]) == 3
    assert Solution().minDeletionSize(["rrjk", "furt", "guzm"]) == 2
