from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[j] >= g[i]:
                ans += 1
                j -= 1

        return ans


assert Solution().findContentChildren(g=[1, 2, 3], s=[1, 1]) == 1
assert Solution().findContentChildren(g=[1, 2], s=[1, 2, 3]) == 2
