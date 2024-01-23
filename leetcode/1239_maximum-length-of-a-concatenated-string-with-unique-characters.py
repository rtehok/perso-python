from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        ans = 0

        def isValid(current_string, next_string):
            s = set()
            for c in next_string:
                if c in s:
                    return False
                s.add(c)
                if c in current_string:
                    return False

            return True

        def dfs(curr, start):
            nonlocal ans
            if ans < len(curr):
                ans = len(curr)

            for i in range(start, n):
                if not isValid(curr, arr[i]):
                    continue
                dfs(curr | set(arr[i]), i + 1)

        dfs(set(), 0)
        return ans


assert Solution().maxLength(["un", "iq", "ue"]) == 4
assert Solution().maxLength(["cha", "r", "act", "ers"]) == 6
assert Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26
