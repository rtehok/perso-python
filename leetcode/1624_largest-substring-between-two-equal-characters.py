import collections


class Solution:
    def maxLengthBetweenEqualCharactersV1(self, s: str) -> int:
        ans = -1
        cnt = collections.defaultdict(list)
        for i, c in enumerate(s):
            cnt[ord(c) - ord("a")].append(i)

        for v in cnt.values():
            if len(v) >= 2:
                ans = max(ans, v[-1] - v[0] - 1)
        return ans

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        first_index = {}

        for i in range(len(s)):
            if s[i] in first_index:
                ans = max(ans, i - first_index[s[i]] - 1)
            else:
                first_index[s[i]] = i
        return ans

assert Solution().maxLengthBetweenEqualCharacters("aa") == 0
assert Solution().maxLengthBetweenEqualCharacters("abca") == 2
assert Solution().maxLengthBetweenEqualCharacters("cbzxy") == -1
