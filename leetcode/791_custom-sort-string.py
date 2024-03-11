import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = collections.Counter(s)
        ans = []
        for c in order:
            if c in cnt:
                ans.append(c * cnt[c])
                cnt.pop(c)

        for c, n in cnt.items():
            ans.append(c * n)

        return "".join(ans)


assert Solution().customSortString(order="cba", s="abcd") == "cbad"
assert Solution().customSortString(order="bcafg", s="abcd") == "bcad"
