from collections import defaultdict


class Solution:
    def firstUniqCharV1(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for i, c in enumerate(s):
            if d[c] == 1:
                return i

        return -1

    def firstUniqChar(self, s: str) -> int:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord("a")] += 1
        for i in range(len(s)):
            if cnt[ord(s[i]) - ord("a")] == 1:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("aabb") == -1
