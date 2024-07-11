from typing import List


class Solution:
    def minOperationsV1(self, logs: List[str]) -> int:
        res = 0
        for step in logs:
            if step == "./":
                continue
            if step == "../" and res > 0:
                res -= 1
            elif step != "../":
                res += 1
        return res

    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for step in logs:
            if step == "../":
                res = max(0, res - 1)
            elif step != "./":
                res += 1
        return res


assert Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]) == 2
assert Solution().minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3
assert Solution().minOperations(logs=["d1/", "../", "../", "../"]) == 0
